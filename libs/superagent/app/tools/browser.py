import aiohttp
from bs4 import BeautifulSoup
from langchain.tools import BaseTool
from security import safe_requests


class Browser(BaseTool):
    name = "Browser"
    description = (
        "a portal to the internet. Use this when you need to "
        "get specific content from a website."
    )
    return_direct = False

    def _run(self, url: str) -> None:
        response = safe_requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        return soup.get_text()

    async def _arun(self, url: str) -> str:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                html_content = await response.text()
                soup = BeautifulSoup(html_content, "html.parser")
                text = soup.get_text()
                return text
