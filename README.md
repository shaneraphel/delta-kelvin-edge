This project was submitted to the ryze.ai hackathon by shan yu.

# On-device interval temperature edge

A local converter that keeps interval temperature (a difference) off the affine Celsius/Kelvin origin. No cloud AI APIs. The optional intent head is a bag-of-words table under 1 MB.

## Run

```bash
python -m delta_kelvin.convert --kind interval --magnitude 3 --target point
```

## Demo

https://shaneraphel.github.io/delta-kelvin-edge/
