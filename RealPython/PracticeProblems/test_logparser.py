from logparser import log_parser


def test_duration_message():
    assert "Device was on for" in ''.join(log_parser("test.log"))


def test_error_message():
    assert "Timestamps of error events:" in log_parser("test.log")


def test_duration():
    assert "Device was on for 7 seconds" in log_parser("test.log")


def test_log_size():
    assert len(log_parser("test.log")) == 4