# Example executables build with `kuibit`

In this directory, we collect working programs built with `kuibit`. You can use
these scripts as good examples of ``kuibit`` usage (or you can directly use
them). There are scripts, `mopi_movies`, and `ciakfiles`, which are
configuration files for [motionpicture](github.com/sbozzolo/motionpicture) (to
make animations) and for [ciak](github.com/sbozzolo/ciak) (to run full
analyses). You are encourages to define the `MOPI_MOVIES_DIR` and the
`CIAKFILES_DIR` to take full advantage of these programs.

> :warning: While `kuibit` is tested at each commit to ensure that nothing
>           breaks, these codes are not. If you find one that does not work,
>           please report it and we will fix that.

## Scripts available

- `plot_grid_var`, plot any 2D grid function on a grid specified via
  command-line.
- `plot_scalar`, plot any reduction of any variable as a time series.
- `plot_1d_vars`, plot one or more along a 1D axis.
- `plot_ah_trajectories`, plot the trajectories of given apparent horizons (in
  3D or a projection on a plane).
- `plot_ah_found`, plot a timeline of when the given horizons are found.
- `plot_ah_separation`, plot the coordinate separation between the centroids of
  two given apparent horizons.
- `plot_ah_radius`, plot the min, max, and mean radius of an apparent horizon as
  a function of time.
- `plot_constraints`, plot the absolute value of the violation of the
  constraints over time.
- `plot_psi4_lm`, plot Psi4 as measured at a given distance and a given multipolar
  decomposition.
- `plot_strain_lm`, plot the strain as measured at a given distance and a given
  multipolar decomposition.
- `plot_phsical_time_per_hour`, plot the computational speed as measured by Carpet's
  `physical_time_per_hour`.
- `plot_gw_energy`, plot the instantaneous power and cumulative energy lost via
   gravitational waves as measured at a given distance.
- `plot_gw_linear_momentum`, plot the instantaneous force and cumulative linear momentum
   along the z direction lost via gravitational waves as measured at a given distance.
- `plot_em_energy`, plot the instantaneous power and cumulative energy lost via
   electromagnetic waves as measured at a given distance.
- `plot_total_luminosity`, plot the total luminosity (gravitational waves +
   electromagnetic waves).
- `plot_MRI_quality_factor`, plot the ratio between the wavelength of the
  magneto-rotational instability and the local resolution of the grid. It requires
  a thorn that computes `MRI_lambda`.
- `print_available_timeseries`, print the list of timeseries that can `kuibit`
  can access.
- `print_available_iterations`, print the list of iterations available for a given
  variable.
- `print_time_formation_ah`, print the time of formation of a given apparent
  horizon.
- `save_reasampled_grid_data`, read a grid function, resamples it to a given grid,
  and save it to a file.
- `load_data_in_mlab`, read a grid function from a file, draw the contour plot, and
  open an interactive `mayavi` session.


## Mopi_movies avaialble

- `1d_vars`, plot a 1D variable as a function of time.
- `grid_var`, plot a 2D variable as a function of time.
- `binary_black_holes`, plot a binary inspiral (see gif below).

<p align="center">
  <img src="https://raw.githubusercontent.com/Sbozzolo/kuibit/experimental/examples/bbh.gif">
</p>

## Ciakfiles avaialble

- `bbh_disk`, for a simulation of accretion onto binary black holes.
- `bbh`, for a simulation of binary black holes.
