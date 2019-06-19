#!/usr/bin/env python
from stm_scheduler import create_app


if __name__ == "__main__":
    app = create_app()
    app.run()
