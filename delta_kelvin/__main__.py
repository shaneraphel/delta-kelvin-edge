from __future__ import annotations

import argparse

from delta_kelvin.convert import convert


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--kind", required=True)
    p.add_argument("--magnitude", type=float, required=True)
    p.add_argument("--target", required=True)
    args = p.parse_args()
    print(convert(args.magnitude, args.kind, args.target))


if __name__ == "__main__":
    main()
