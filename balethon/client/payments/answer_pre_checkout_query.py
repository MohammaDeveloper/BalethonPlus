import balethon


class AnswerPreCheckoutQuery:
    async def answer_pre_checkout_query(
        self: "balethon.Client",
        pre_checkout_query_id: str,
        ok: bool = True,
        error_message: str = None,
    ) -> bool:
        if not ok and error_message is None:
            error_message = "لطفاً بعدا دوباره تلاش کنید."
        return await self.auto_execute("post", "answerPreCheckoutQuery", locals())
