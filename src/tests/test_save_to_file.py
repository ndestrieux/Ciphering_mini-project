from pathlib import Path
from unittest.mock import call, mock_open, patch

from utils.manager import Manager


class TestSaveToFile:
    @patch("utils.manager.Manager.get_data_from_memory")
    @patch("builtins.open", new_callable=mock_open)
    def test_save_to_file(self, mocked_open, memory_mock):
        def mocked_memory():
            return {
                "ROT47": [
                    "test",
                ],
                "ROT13": [
                    "Hello",
                    "World",
                ],
            }

        memory_mock.side_effect = mocked_memory
        m = Manager()
        m.save_to_file()
        mocked_open.return_value.write.assert_has_calls(
            [call("test\n"), call("Hello\n"), call("World\n")]
        )
        mocked_open.assert_called_with(Path("../utils/data/ROT13"), "a+")
