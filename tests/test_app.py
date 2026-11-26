import os
import unittest
from unittest.mock import MagicMock, patch

import app as motivation_app


class MotivationAppTestCase(unittest.TestCase):
    def setUp(self):
        motivation_app.app.config["TESTING"] = True
        self.client = motivation_app.app.test_client()

    def test_home_page_renders_template_and_assets(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        html = response.get_data(as_text=True)
        self.assertIn("Daily Motivation Generator", html)
        self.assertIn("/static/style.css", html)
        self.assertIn("/static/script.js", html)

    def test_health_endpoint(self):
        with patch.dict(os.environ, {"OPENAI_API_KEY": ""}, clear=False):
            response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data["status"], "ok")
        self.assertFalse(data["openai_configured"])

    def test_generate_motivation_fallback_without_api_key(self):
        with patch.dict(os.environ, {"OPENAI_API_KEY": ""}, clear=False):
            response = self.client.post(
                "/generate_motivation", json={"mood": "needs focus"}
            )
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data["mood"], "needs focus")
        self.assertEqual(data["source"], "fallback")
        self.assertTrue(len(data["motivation"]) > 0)

    def test_generate_motivation_rejects_empty_mood(self):
        response = self.client.post("/generate_motivation", json={"mood": "   "})
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.get_json())

    def test_generate_motivation_with_mocked_openai(self):
        mock_choice = MagicMock()
        mock_choice.message.content = "Keep building—every bug you fix makes you sharper."
        mock_response = MagicMock(choices=[mock_choice])

        mock_client = MagicMock()
        mock_client.chat.completions.create.return_value = mock_response

        with patch.dict(os.environ, {"OPENAI_API_KEY": "sk-test-key"}, clear=False):
            with patch.object(motivation_app, "OpenAI", return_value=mock_client):
                response = self.client.post(
                    "/generate_motivation", json={"mood": "unmotivated"}
                )

        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data["source"], "openai")
        self.assertEqual(
            data["motivation"], "Keep building—every bug you fix makes you sharper."
        )

    def test_feedback_endpoint_validation_and_success(self):
        bad = self.client.post("/feedback", json={"name": "", "feedback": ""})
        self.assertEqual(bad.status_code, 400)

        ok = self.client.post(
            "/feedback", json={"name": "Vikash", "feedback": "Works great!"}
        )
        self.assertEqual(ok.status_code, 201)
        self.assertEqual(ok.get_json()["status"], "received")


if __name__ == "__main__":
    unittest.main()
