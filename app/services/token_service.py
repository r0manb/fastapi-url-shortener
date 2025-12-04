import datetime as dt

import jwt


class _TokenService:
    _secret_key: str
    _exp: dt.timedelta
    _algorithm: str

    def __init__(
        self, secret_key: str, exp_params: dict[str, int], algorithm: str = "HS256"
    ) -> None:
        self._secret_key = secret_key
        self._exp = dt.timedelta(**exp_params)
        self._algorithm = algorithm

    def generate_token(self, payload: dict) -> str:
        issued_at = dt.datetime.now(tz=dt.timezone.utc)
        token = jwt.encode(
            payload={
                **payload,
                "exp": issued_at + self._exp,
                "iat": issued_at,
                "nbf": issued_at,
            },
            key=self._secret_key,
            algorithm="HS256",
        )

        return token

    def verify_token(self, token: str) -> dict | None:
        try:
            return jwt.decode(
                jwt=token, key=self._secret_key, algorithms=(self._algorithm,)
            )
        except Exception as e:
            print(e)
            return None
