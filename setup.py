from setuptools import setup

if __name__ == "__main__":
    setup(
        use_scm_version={"write_to": "src/xdist/_version.py"},
    )
