import sys


def load_corpus(corpus_path):
    """
    Return the data contained within a specified corpus.
    """
    from chatterbot.utils.module_loading import import_module

    corpus = import_module(corpus_path)

    corpora = []

    if hasattr(corpus, 'modules'):
        for module_name in corpus.modules:
            module = import_module(corpus_path + module_name)

            corpora += module.data

        return corpora

    return [corpus.data]

