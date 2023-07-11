import argparse
import yaml

from src.outils.outils import Outils

parser = argparse.ArgumentParser()
parser.add_argument("--config", type=str, required=True, help="path to yaml config")
args = parser.parse_args()

with open(args.config, mode="r") as stream:
    config = yaml.safe_load(stream)




if __name__=="__main__":
    parser = Outils()
    parser.modulo(config)

