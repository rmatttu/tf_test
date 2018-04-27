# vim: fileencoding=utf-8

import numpy as np
import pet_dataset


def main():
    dataset = pet_dataset.PetDataset()
    dataset.load()
    batch = dataset.generate_batch()
    import pdb; pdb.set_trace()


if __name__ == '__main__':
    main()
