import os


def get_shots_path(instance, filename):
    return os.path.join('products', "product_%s" % str(instance.id), filename)


def get_results_path(instance, filename):
    return os.path.join('results', "results_%s" % str(instance.id), filename)
