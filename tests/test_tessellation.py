import numpy as np
import pytest
from ndh_canvas_adapter.tessellation import TessellationBeeCore


def test_tessellation_core_initialization():
    """Verifies that the engine initializes with correct defaults."""
    core = TessellationBeeCore()
    assert core.dims == 80
    assert core.epsilon == 1e-9


def test_normalization_shape_handling():
    """Ensures input vectors match required dimensional constraints."""
    core = TessellationBeeCore(target_dimensions=80)

    # Invalid dimension shape should raise a ValueError
    invalid_input = np.random.rand(5, 79)
    with pytest.raises(ValueError):
        core.normalize_phase_space(invalid_input)


def test_projection_pipeline():
    """Validates vector reduction from 80D arrays into discrete studio zones."""
    core = TessellationBeeCore(target_dimensions=80)
    mock_80d_data = np.random.uniform(-10.0, 10.0, size=(3, 80))

    bins = core.project_to_canvas_bins(mock_80d_data, grid_resolution=12)

    assert len(bins) == 3
    for operational_bin in bins:
        assert "layout_bin" in operational_bin
        assert "color_index" in operational_bin
        
        # Verify 2D constraints
        x, y = operational_bin["layout_bin"]
        assert 0 <= x < 12
        assert 0 <= y < 12
        assert 0 <= operational_bin["color_index"] <= 255
