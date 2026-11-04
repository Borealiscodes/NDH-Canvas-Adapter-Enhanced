import numpy as np


class TessellationBeeCore:
    """Manages high-dimensional phase space projections and 2D canvas zoning."""

    def __init__(self, target_dimensions: int = 80, epsilon_safety: float = 1e-9):
        self.dims = target_dimensions
        self.epsilon = epsilon_safety

    def normalize_phase_space(self, coordinates: np.ndarray) -> np.ndarray:
        """Applies radial diffusion constraints and apex vector normalization."""
        coords = np.array(coordinates, dtype=float)
        if coords.shape[-1] != self.dims:
            raise ValueError(f"Expected a matrix containing {self.dims}D vector arrays.")

        # Compute L2 norms with an epsilon floor to prevent structural representation crowding
        norms = np.linalg.norm(coords, axis=-1, keepdims=True)
        norms = np.maximum(norms, self.epsilon)

        return coords / norms

    def project_to_canvas_bins(
        self, coordinates: np.ndarray, grid_resolution: int = 10
    ) -> list[dict]:
        """Maps high-dimensional coordinate arrays down to deterministic 2D layout bins.

        Simulates barycentric structural grid distributions for deterministic studio practices.
        """
        normalized_vectors = self.normalize_phase_space(coordinates)

        # Map high-dimensional slices to 2D space via localized projections
        x_proj = np.mean(normalized_vectors[..., 0 : self.dims // 2], axis=-1)
        y_proj = np.mean(normalized_vectors[..., self.dims // 2 :], axis=-1)

        # Scale and bin coordinates into static structural grids
        x_bins = np.clip(
            ((x_proj + 1.0) / 2.0 * grid_resolution).astype(int), 0, grid_resolution - 1
        )
        y_bins = np.clip(
            ((y_proj + 1.0) / 2.0 * grid_resolution).astype(int), 0, grid_resolution - 1
        )

        binned_layouts = []
        for x, y in zip(x_bins.flatten(), y_bins.flatten()):
            # Calculate high-probability indices for deterministic chromatic zones
            color_index = int((x * 7 + y * 13) % 256)
            binned_layouts.append({"layout_bin": (int(x), int(y)), "color_index": color_index})

        return binned_layouts
