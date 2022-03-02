from wos_api_wrapper.wos.user_query_search import UserQuerySearch

import time

database_id = "WOS"
query = "OG=({Far Eastern Federal University})"
count = 5
first = 1
header1 = UserQuerySearch(
    database_id=database_id,
    query=query,
    records_count=count,
    first_record=first,
    download=True,
    use_cache=True
).get_response_headers()

print("first header:")
print(header1)

time.sleep(2)

header2 = UserQuerySearch(
    database_id=database_id,
    query=query,
    records_count=count,
    first_record=first,
    download=True,
    use_cache=True
).get_response_headers()

print(f"second header: {type(header2)}")
print(header2)

assert str(header1) == str(header2), "\nThe response was not downloaded or correctly loaded from cache\n"
print("RESPONSE CACHING: SUCCESS\n\n\n")
