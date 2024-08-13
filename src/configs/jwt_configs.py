import os

jwt_infos = {
  "JWT_KEY": os.getenv("JWT_KEY"),
  "JWT_ALGORITHM": os.getenv("JWT_ALGORITHM"),
  "JWT_EXP": int(os.getenv("JWT_EXP"))
}
