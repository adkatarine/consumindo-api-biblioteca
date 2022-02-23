from environs import Env

env = Env()
env.read_env()

library_url = {
    "works_url": env("API_LIBRARY_WORK_URL"),
}
