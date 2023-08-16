from pydantic import BaseModel, ValidationError


class User(BaseModel):
    field_a: str
    field_b: int | None = None


external_data = {
    "field_a": "foo",
    "field_b": 1,
}  # pydantic.mypyなしの場合はtyping.Anyを指定する必要がある。

try:
    user = User(**external_data)

    # mypyでのチェック時にエラーが発生する。
    # error: "User" has no attribute "field_c"; maybe "field_a" or "field_b"?  [attr-defined]
    print(user.field_c)
except ValidationError as e:
    print(e)
