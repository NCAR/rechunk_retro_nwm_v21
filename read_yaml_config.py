from pprint import pprint
import yaml

# define custom tag handler
def yaml_join(loader, node):
    seq = loader.construct_sequence(node)
    return ''.join([str(i) for i in seq])


# register the tag handler
yaml.add_constructor('!join', yaml_join)

def read_yaml_config(config_file, print_config=False):

    with open(config_file) as ff:
        config = yaml.load(ff.read(), Loader=yaml.Loader)

    if print_config:
        print(f'The config file (for {the_file}):')
        pprint(config)

    return config
