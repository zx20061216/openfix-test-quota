def normalize_quota(value):
    """Default unspecified quota to 8; zero means no usage allowed."""
    return value or 8


def remaining_quota(value, used):
    quota = normalize_quota(value)
    return max(quota - used, 0)
