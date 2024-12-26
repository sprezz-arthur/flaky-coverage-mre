from multiprocessing.pool import Pool
from typing import Any


class SinucaMultiprocessingPool(Pool):
    def __exit__(self, *args, **kwargs: Any):
        self.close()
        self.join()
        super().__exit__(*args, **kwargs)


Pool = SinucaMultiprocessingPool
