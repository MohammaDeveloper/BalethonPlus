from random import randint
from time import time

from httpx import AsyncClient
from httpx._config import DEFAULT_TIMEOUT_CONFIG
from httpx._types import ProxyTypes, TimeoutTypes

from ..errors import RPCError
from ..sync_support import add_sync_support_to_object


@add_sync_support_to_object
class OTPClient:
    BASE_URL = "https://safir.bale.ai"

    def __init__(
        self,
        id: str,
        secret: str,
        time_out: TimeoutTypes = DEFAULT_TIMEOUT_CONFIG,
        proxy: ProxyTypes = None,
    ):
        self.id = id
        self.secret = secret
        self.time_out = time_out
        self.proxy = proxy
        self.expires_time_last_access_token = 0.000
        self.last_access_token = None
        self.client = None
        self.is_started = False

    async def connect(self):
        if self.is_started:
            raise ConnectionError("Connection is already started")
        self.is_started = True
        self.client = AsyncClient(proxy=self.proxy, timeout=self.time_out)

    async def disconnect(self):
        if not self.is_started:
            raise ConnectionError("Connection is already stopped")
        self.is_started = False
        await self.client.aclose()
        self.client = None

    async def __aenter__(self):
        await self.connect()
        return self

    async def __aexit__(self, *args):
        try:
            await self.disconnect()
        except ConnectionError:
            return

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, *args):
        try:
            self.disconnect()
        except ConnectionError:
            return

    async def get_auth_token(self):
        current_time = time()

        if self.last_access_token:
            if current_time - self.expires_time_last_access_token < 0:
                return self.last_access_token

        response = await self.client.post(
            f"{self.BASE_URL}/api/v2/auth/token",
            headers={
                "Content-Type": "application/x-www-form-urlencoded",
            },
            params={
                "grant_type": "client_credentials",
                "client_secret": self.secret,
                "scope": "read",
                "client_id": self.id,
            },
        )
        status_code = response.status_code
        if status_code != 200:
            if status_code == 400:
                description = "Failed to Parse Request"
            elif status_code == 401:
                description = "Client authentication failed"
            elif status_code == 500:
                description = "Internal server error occurred"
            raise RPCError.create(status_code, description)
        response_json = response.json()
        self.last_access_token = response_json["access_token"]
        self.expires_time_last_access_token = current_time + response_json["expires_in"]
        return self.last_access_token

    async def send_otp(self, phone: str, otp: int):
        response = await self.client.post(
            f"{self.BASE_URL}/api/v2/send_otp",
            headers={
                "Authorization": f"Bearer {await self.get_auth_token()}",
                "Content-Type": "application/json",
            },
            json={
                k: v
                for k, v in zip(list(locals().keys())[1:], list(locals().values())[1:])
            },
        )
        response_json = response.json()
        if response.status_code != 200:
            description = response_json.get("message")
            raise RPCError.create(
                response.status_code,
                description.capitalize() if description else description,
            )
        return response_json.get("balance")

    def passcode_generate(self, number_of_digits: int = 5) -> int:
        return int("".join([str(randint(1, 9)) for _ in range(number_of_digits)]))
