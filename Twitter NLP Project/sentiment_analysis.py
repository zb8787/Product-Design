import argparse

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

def analyze(the_filename):
    """Run a sentiment analysis request on text within a passed filename."""
    client = language.LanguageServiceClient()

    with open(the_filename, "r", encoding="utf8") as the_file:
        # Instantiates a plain text document.
        content = the_file.read()

    document = types.Document(content=content, type=enums.Document.Type.PLAIN_TEXT)
    annotations = client.analyze_sentiment(document=document)

    # Print the results
    print_result(annotations)
	
def print_result(annotations):
"""Print result of sentiment analysis"""
    score = annotations.document_sentiment.score
    magnitude = annotations.document_sentiment.magnitude

    for index, sentence in enumerate(annotations.sentences):
        sentence_sentiment = sentence.sentiment.score
        print(
            "Sentence {} has a sentiment score of {}".format(index, sentence_sentiment)
        )

    print(
        "Overall Sentiment: score of {} with magnitude of {}".format(score, magnitude)
    )
    return 0

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "the_filename",
        help="The filename of the tweet you'd like to analyze.",
    )
    args = parser.parse_args()

    analyze(args.the_filename)
