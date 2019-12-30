class ProjectList:
    def __init__(self, projects=[]):
        self.projects = projects


class Project:
    def __init__(self, name, depend_on=[]):
        self.name = name
        self.depend_on = depend_on
        self.is_done = False


def get_execution_order(project_list):

    return _get_execution_order(project_list.projects)


def _get_execution_order(project_list, root=None, order=[]):
    if project_list == []:
        return order

    project = project_list[0]

    if root is None:
        root = project

    if project == root:
        raise ValueError()

    if project.is_done:
        return _get_execution_order(project_list[1:], order)

    if project.depend_on:
        order.extend(_get_execution_order(project.depend_on, root=project, order=[]))

    order.append(project.name)
    project.is_done = True
    return _get_execution_order(project_list[1:], order)
