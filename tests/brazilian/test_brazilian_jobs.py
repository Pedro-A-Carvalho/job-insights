from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    result = read_brazilian_file("tests/mocks/brazilians_jobs.csv")

    # Assert
    for job in result:
        assert "title" in job
        assert "salary" in job
        assert "type" in job
