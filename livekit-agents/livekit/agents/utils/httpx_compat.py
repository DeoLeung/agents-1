"""Compatibility helpers for OpenAI's httpx2 transport."""

from __future__ import annotations

import httpx
import httpx2


def as_httpx2_timeout(timeout: httpx.Timeout) -> httpx2.Timeout:
    """Convert the public LiveKit timeout type to OpenAI 3's httpx2 timeout."""
    return httpx2.Timeout(
        timeout.read,
        connect=timeout.connect,
        write=timeout.write,
        pool=timeout.pool,
    )
