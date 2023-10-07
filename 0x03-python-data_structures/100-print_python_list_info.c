#include <Python.h>

/**
 * print_python_list_info - Prints basic info about Python lists.
 * @p: A PyObject list.
 */
void print_python_list_info(PyObject *p)
{
	if (PyList_Check(p))
	{
		Py_ssize_t size = PyList_Size(p);
		Py_ssize_t allocated = ((PyListObject *)p)->allocated;

		printf("[*] Size of the Python List = %d\n", size);
		printf("[*] Allocated = %d\n", alloc);
		for (i = 0; i < size; i++)
		{
		printf("Element %d: ", i);
		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
		}
	}
	else
	{
		fprintf(stderr, "Invalid Python List\n");
	}
}
