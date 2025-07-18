from random import randint

from httpx import AsyncClient
from httpx._config import DEFAULT_TIMEOUT_CONFIG
from httpx._types import ProxyTypes, TimeoutTypes

from ..errors import RPCError
from ..sync_support import add_sync_support_to_object


@add_sync_support_to_object
class Client:
    URL = "https://safir.bale.ai"

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
        self.client = AsyncClient(proxy=self.proxy, timeout=self.time_out)

    def __repr__(self):
        return f"{type(self).__name__}({self.id})"

    async def connect(self):
        return

    async def disconnect(self):
        await self.client.aclose()

    async def __aenter__(self):
        await self.connect()
        return self

    async def __aexit__(self, *args):
        await self.disconnect()

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, *args):
        self.disconnect()

    async def get_auth_token(self) -> str:
        response = await self.client.post(
            f"{self.URL}/api/v2/auth/token",
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            params={
                "grant_type": "client_credentials",
                "client_secret": self.secret,
                "scope": "read",
                "client_id": self.id,
            },
        )

        response_json = response.json()

        if response.status_code != 200:
            raise RPCError.create(response.status_code, response_json)

        return response_json["access_token"]

    async def send_otp(self, phone: str, otp: int):
        token = await self.get_auth_token()

        json = locals()
        del json["self"]

        response = await self.client.post(
            f"{self.URL}/api/v2/send_otp",
            headers={
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json",
            },
            json=json,
        )

        response_json = response.json()

        if response.status_code != 200:
            description = response_json.get("message")
            raise RPCError.create(
                response.status_code,
                description.capitalize() if description else description,
                "send_otp",
            )

    @staticmethod
    def passcode_generate(number_of_digits: int = 5) -> int:
        return int("".join(str(randint(1, 9)) for _ in range(number_of_digits)))
