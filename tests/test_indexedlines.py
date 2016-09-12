import os.path
from openfile import openfile
from indexedlines import IndexedLines


def test_indexedlines(tmpdir):
    tmpdir = str(tmpdir)
    fname = os.path.join(tmpdir, "test.txt")
    lines = ["%d\n" % (i,) for i in range(1000)]
    with openfile(fname, "wt") as f:
        f.write("".join(lines))
    assert not os.path.exists(fname + ".idx")
    with IndexedLines(fname) as ilines:
        assert lines == list(ilines)
    assert os.path.exists(fname + ".idx")
    with IndexedLines(fname) as ilines:
        assert lines == list(ilines)
