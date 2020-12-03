import sentiment_analysis as sa

filename = "hashtag.txt"
annotations = "anno_SAMPLE.txt"

def test_analyze():
	assert not sa.analyze(filename)
def test_printresult():
    assert not sa.print_result(annotations)