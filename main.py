import config
import node
import output


def main():
    conf = config.Config()
    nodes = node.get_nodes(conf.get("place"), conf.get("all"))
    # we have two case, either we want the list of persons, or we want the status
    output.make(nodes, conf.get("list"))

if __name__ == '__main__':
    main()