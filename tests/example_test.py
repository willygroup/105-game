import unittest
import os

# pylint: disable=import-error
from commons import prepare_env, restore_env

# pylint: disable=import-error
from modules.example_mod import Example


class TestExampleModule(unittest.TestCase):
    def get_dirname(self) -> str:
        dirname = os.path.realpath(__file__)
        dirname = os.path.split(dirname)[0]
        return dirname

    def test_init_example_without_args(self):

        tmp_dirs = prepare_env("test_init_example")

        example = Example()

        self.assertEqual(example.value, 0)

        restore_env(tmp_dirs)

    def test_init_example_with_args(self):

        tmp_dirs = prepare_env("test_init_example")

        example = Example(42)

        self.assertEqual(example.value, 42)

        restore_env(tmp_dirs)


if __name__ == "__main__":
    unittest.main()
