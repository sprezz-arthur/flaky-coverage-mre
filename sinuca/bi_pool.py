from typing import Any

from billiard.pool import Pool


class SinucaBilliardPool(Pool):
    def __exit__(self, *args, **kwargs: Any):
        self.close()
        self.join()
        super().__exit__(*args, **kwargs)


Pool = SinucaBilliardPool
