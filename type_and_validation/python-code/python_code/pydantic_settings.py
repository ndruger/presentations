from pydantic import ValidationError
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    use_great_option: bool = False


try:
    settings = Settings()
    print(settings.use_great_option)
    # use_great_option="true" -> True
    # use_great_option="True" -> True
    # use_great_option="1" -> True
    # use_great_option="false" -> False
    # use_great_option="False" -> False
    # use_great_option="0" -> False
except ValidationError as e:
    # use_great_option="aaa" -> ValidationError
    # use_great_option="" -> ValidationError
    print(e)
