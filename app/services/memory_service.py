# Simple in-memory storage (hackathon version)

USER_MEMORY = {}


def save_user_data(user_id: str, data: dict):
    USER_MEMORY[user_id] = data


def get_user_data(user_id: str):
    return USER_MEMORY.get(user_id, {})