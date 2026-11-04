"""
test_geometry.py
Target Framework: NDH-Canvas-Adapter-Enhanced
Domain: Pytest Suite for Boundary Containment Metrics
Status: Production-Ready Verification Script
"""

import pytest
import numpy as np
from src.ndh_canvas_adapter.lh_adapter import LeanHallucinationGuard

@pytest.fixture
def default_guard():
    """Initializes a standard guard instance mimicking the Lean 4 vault parameters."""
    return LeanHallucinationGuard(epsilon=1e-6, max_condition_number=4.5)

def test_norm_safety_floor_prevents_zero_division(default_guard):
    """
    Validates that the safety floor handles absolute zero norms.
    Mirrors the Lean 4 'norm_safety_floor' theorem loop.
    """
    zero_vector = np.zeros(80)
    
    # Process vector through the projection core
    projected = default_guard.project_to_hypersphere(zero_vector)
    
    # Assert that processing completed smoothly without throwing a ZeroDivisionError
    assert isinstance(projected, np.ndarray)
    assert projected.shape == (80,)
    # Under a zero norm, the fallback system must reduce the state vector to a safe zero baseline
    assert np.allclose(projected, 0.0)

def test_hypersphere_projection_invariant_containment(default_guard):
    """
    Validates that extreme, drifting, or sprawling input coordinate spikes
    are squashed completely down inside the invariant bounded unit radius.
    Mirrors the Lean 4 'hypersphere_projection_invariant' theorem statement.
    """
    # Create extreme coordinate drift values (simulating a runaway AI explosion)
    extreme_vectors = [
        np.ones(80) * 1e9,                 # Massive coordinate explosion
        np.random.randn(80) * 500.0,       # Scattered explosive noise
        np.ones(80) * (default_guard.epsilon / 2.0) # Sub-epsilon micro-state
    ]
    
    for vec in extreme_vectors:
        projected = default_guard.project_to_hypersphere(vec)
        norm_val = np.linalg.norm(projected)
        
        # Rigorous boundary assertion: Norm MUST fall strictly inside the closed hypersphere unit bound
        assert norm_val <= 1.0 + 1e-12, f"Hypersphere projection breach: norm {norm_val} exceeded 1.0"

def test_verify_manifold_matrix_catches_geometric_collapse(default_guard):
    """
    Verifies that the rolling SVD checks properly intercept collapsing manifolds
    where condition matrix limits are exceeded (κ₂ > 4.5).
    """
    # Generate a perfectly stable identity frame
    stable_matrix = np.eye(80)
    is_safe, cond_num = default_guard.verify_manifold_matrix(stable_matrix)
    assert is_safe == True
    assert np.isclose(cond_num, 1.0)
    
    # Generate a highly unstable, collapsing matrix field (forcing extreme singular values)
    collapsing_matrix = np.eye(80)
    collapsing_matrix[0, 0] = 1e6     # Extreme stretch along primary axis
    collapsing_matrix[1, 1] = 1e-12   # Deep collapse into near-zero dimensionality
    
    is_safe, cond_num = default_guard.verify_manifold_matrix(collapsing_matrix)
    
    # The intercept guard must catch this and signal a safety reject flag
    assert is_safe == False
    assert cond_num > default_guard.max_condition_number

def test_deterministic_abort_handler_gatekeeping(default_guard):
    """
    Ensures that processing an entirely invalid, unstable matrix data array
    reliably returns None to signal the master script to execute automated 
    rapid Z-axis hardware lifts (whitespace generation).
    """
    # Create an illegal matrix frame size that breaches dimension laws
    illegal_shape_matrix = np.random.randn(10, 10)
    
    result = default_guard.process_telemetry_frame(frame_id=99, raw_manifold_data=illegal_shape_matrix)
    assert result is None
    
    # Create a mathematically legal shape, but structurally unsafe collapsing vector profile
    unsafe_collapsing_matrix = np.zeros((80, 80)) # Complete coordinate void
    
    result = default_guard.process_telemetry_frame(frame_id=100, raw_manifold_data=unsafe_collapsing_matrix)
    assert result is None
