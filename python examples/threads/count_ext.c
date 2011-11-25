/* file: count_ext.c */

#include <Python.h>                          /*1*/

int count (int n);                           /*2*/

static PyObject *                            /*3*/
calc_count(PyObject *self, PyObject *args)    /*4*/
    {
    int n, count_inside;

    if (!PyArg_ParseTuple(args, "i", &n))    /*5*/
        return NULL;                         /*6*/
    Py_BEGIN_ALLOW_THREADS                   /*7*/
    count_inside = count(n);                 /*8*/
    Py_END_ALLOW_THREADS                     /*9*/
    return Py_BuildValue("i", count_inside); /*10*/
    }


static PyMethodDef funcs[] = {               /*11*/
    {"count",  calc_count, METH_VARARGS,
     "Counts the number of points inside circle."},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

void
initcount_ext(void)                          /*12*/
    {
    Py_InitModule3("count_ext", funcs,       /*13*/
     "Example for extending Python by hand.");
    }
    