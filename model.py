def reconstruct(request):
    """Return a complete time-by-channel matrix for this telemetry window."""
    return [[0.0 if value is None else value for value in row]
            for row in request['values']]
