from dataclasses import dataclass


@dataclass
class MyTestClass:
    test_attribute: str

    def my_test_function(self) -> bool:
        return True
