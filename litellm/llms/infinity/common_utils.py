from typing import Union
import httpx

from litellm.llms.base_llm.chat.transformation import BaseLLMException


class InfinityError(BaseLLMException):
    def __init__(
        self, 
        status_code: int, 
        message: str,
        headers: Union[dict, httpx.Headers] = {}
        ):
        self.status_code = status_code
        self.message = message
        self.request = httpx.Request(
            method="POST", url="https://github.com/michaelfeil/infinity"
        )
        self.response = httpx.Response(status_code=status_code, request=self.request)
        super().__init__(
            status_code=status_code,
            message=message,
            request=self.request,
            response=self.response,
            headers=headers,
        )  # Call the base class constructor with the parameters it needs
