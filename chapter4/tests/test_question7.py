import pytest

from chapter4.question7 import (
    ProjectList,
    Project,
    get_execution_order,
)


@pytest.fixture
def project_list1():
    """ 通常のパターン """
    project_a = Project(name="a")
    project_b = Project(name="b")
    project_c = Project(name="c")
    project_d = Project(name="d")
    project_e = Project(name="e")
    project_f = Project(name="f")

    project_d.depend_on = [project_a, project_b]
    project_b.depend_on = [project_f]
    project_a.depend_on = [project_f]
    project_c.depend_on = [project_d]

    return ProjectList(
        [project_a, project_b, project_c, project_d, project_e, project_f]
    )


@pytest.fixture
def project_list2():
    """ デッドロックになっているパターン """
    project_a = Project(name="a")
    project_b = Project(name="b")
    project_c = Project(name="c")

    project_a.depend_on = [project_b]
    project_b.depend_on = [project_c]
    project_c.depend_on = [project_a]

    return ProjectList([project_a, project_b, project_c])


def test_get_execution_order1(project_list1):
    assert get_execution_order(project_list1) == ["f", "a", "b", "d", "c", "e"]


def test_get_execution_order2(project_list2):
    with pytest.raises(ValueError):
        get_execution_order(project_list2)
