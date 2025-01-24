import os
test_files = [
    "test_execution/test_banner",
    "test_execution/test_category",
    "test_execution/test_ps5",
    "test_execution/test_search",
    "test_execution/test_social_media",
    "test_execution/test_region"

]
for test_file in test_files:
    os.system(f"pytest{test_file}")