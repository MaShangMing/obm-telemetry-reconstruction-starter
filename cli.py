import json
import sys
import resource

# The candidate is a single-process component, including during module import.
resource.setrlimit(resource.RLIMIT_NPROC, (1, 1))
from model import reconstruct

for line in sys.stdin:
    request = json.loads(line)
    result = reconstruct(request)
    print(json.dumps({'values': result}, allow_nan=False, separators=(',', ':')), flush=True)
