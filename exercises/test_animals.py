#!/usr/bin/env python3

"""
Script to test the animals package.
"""

import animals

# Test the Birds classes:
dangerous_b = animals.dangerous.Birds()
dangerous_b.printMembers()

harmless_b = animals.harmless.Birds()
harmless_b.printMembers()

# Test the Mammals classes:
dangerous_m = animals.dangerous.Mammals()
dangerous_m.printMembers()

harmless_m = animals.harmless.Mammals()
harmless_m.printMembers()

# Test the Fish classes:
dangerous_f = animals.dangerous.Fish()
dangerous_f.printMembers()

harmless_f = animals.harmless.Fish()
harmless_f.printMembers()

