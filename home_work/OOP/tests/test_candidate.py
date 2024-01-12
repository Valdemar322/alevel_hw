from unittest import TestCase
from _18.oop_candidate import Candidate


class TestCandidate(TestCase):
    def test_candidate_full_name(self):
        candidates = Candidate.generate_candidates("candidates.csv")
        self.assertEqual(candidates[0].full_name, "Ivan Chechov")
        self.assertEqual(candidates[1].full_name, "Max Payne")
        self.assertEqual(candidates[2].full_name, "Tom Hanks")

    def test_candidate_generate_candidates(self):
        candidates = Candidate.generate_candidates("candidates.csv")
        self.assertEqual(candidates[0].first_name, "Ivan")
        self.assertEqual(candidates[0].last_name, "Chechov")
        self.assertEqual(candidates[0].email, "ichech@example.com")
        self.assertEqual(candidates[0].tech_stack, "Python|Django|Angular")
        self.assertEqual(candidates[0].main_skill, "Python")
        self.assertEqual(candidates[0].main_skill_grade, "Senior")

        self.assertEqual(candidates[1].first_name, "Max")
        self.assertEqual(candidates[1].last_name, "Payne")
        self.assertEqual(candidates[1].email, "mpayne@example.com")
        self.assertEqual(candidates[1].tech_stack, "PHP|Laravel|MySQL")
        self.assertEqual(candidates[1].main_skill, "PHP")
        self.assertEqual(candidates[1].main_skill_grade, "Middle")

        self.assertEqual(candidates[2].first_name, "Tom")
        self.assertEqual(candidates[2].last_name, "Hanks")
        self.assertEqual(candidates[2].email, "thanks@example.com")
        self.assertEqual(candidates[2].tech_stack, "Python|CSS")
        self.assertEqual(candidates[2].main_skill, "Python")
        self.assertEqual(candidates[2].main_skill_grade, "Junior")
