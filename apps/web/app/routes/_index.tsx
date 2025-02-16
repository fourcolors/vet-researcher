import type { ActionFunctionArgs, MetaFunction } from "@remix-run/node";
import { Form, useActionData, useNavigation } from "@remix-run/react";
import { Info, Loader2, Send } from "lucide-react";
import { useRef } from "react";
import { BackgroundBeams } from "~/components/background-beams";
import { Button } from "~/components/ui/button";
import { Textarea } from "~/components/ui/textarea";

export const meta: MetaFunction = () => {
  return [
    { title: "Vet Researcher - Verify Pet Symptoms" },
    {
      name: "description",
      content: "Verify your pet's symptoms in seconds with AI-powered analysis",
    },
  ];
};

export async function action({ request }: ActionFunctionArgs) {
  const formData = await request.formData();
  const symptoms = formData.get("symptoms");

  if (!symptoms) {
    return {
      error: "Please enter your pet's symptoms",
    };
  }

  try {
    // Check if API is available
    try {
      const healthCheck = await fetch("http://localhost:8000/health");
      if (!healthCheck.ok) {
        throw new Error("API is not available");
      }
    } catch (e) {
      throw new Error(
        "Unable to connect to the API. Please try again in a moment."
      );
    }

    // Call API endpoint
    const response = await fetch("http://localhost:8000/analyze", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ query: symptoms }),
    });

    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.detail || "Failed to analyze symptoms");
    }

    const data = await response.json();
    return data;
  } catch (error) {
    return {
      error:
        error instanceof Error ? error.message : "Failed to analyze symptoms",
    };
  }
}

export default function Index() {
  const actionData = useActionData<typeof action>();
  const navigation = useNavigation();
  const formRef = useRef<HTMLFormElement>(null);
  const isSubmitting = navigation.state === "submitting";

  return (
    <div className="min-h-screen w-full relative overflow-hidden flex items-center justify-center bg-gray-50">
      <BackgroundBeams />
      <div className="max-w-4xl w-full mx-auto px-4 sm:px-6 lg:px-8 z-10">
        <div className="text-center space-y-8">
          <h1 className="text-4xl md:text-6xl font-[800] text-center bg-clip-text text-transparent bg-gradient-to-r from-blue-600 via-blue-800 to-purple-700 drop-shadow-sm tracking-tight leading-[1.15]">
            Verify Pet Symptoms <br />
            In Seconds
          </h1>

          <div className="w-full space-y-4">
            {!actionData?.result && (
              <Form ref={formRef} method="post" className="relative">
                <Textarea
                  name="symptoms"
                  className="w-full min-h-[200px] bg-white/70 text-gray-800 border-gray-300 rounded-lg p-4 text-lg resize-none backdrop-blur-sm disabled:opacity-50"
                  placeholder="Enter your pet's symptoms here..."
                  disabled={isSubmitting}
                />
                <Button
                  type="submit"
                  className="absolute right-4 bottom-4 bg-blue-600 hover:bg-blue-700 text-white disabled:opacity-50"
                  size="icon"
                  disabled={isSubmitting}
                >
                  {isSubmitting ? (
                    <Loader2 className="h-4 w-4 animate-spin" />
                  ) : (
                    <Send className="h-4 w-4" />
                  )}
                </Button>
              </Form>
            )}

            {actionData?.error && (
              <div className="bg-red-50 border border-red-200 rounded-lg p-4">
                <p className="text-red-600">{actionData.error}</p>
                <Button
                  onClick={() => formRef.current?.reset()}
                  className="mt-2 text-red-600 hover:text-red-700"
                  variant="link"
                >
                  Try again
                </Button>
              </div>
            )}

            {actionData?.result && (
              <div className="space-y-4">
                <div className="bg-white/70 backdrop-blur-sm rounded-lg border border-gray-300 p-6 shadow-lg">
                  <h3 className="text-lg font-semibold text-gray-800 mb-2">
                    Analysis Result
                  </h3>
                  <p className="text-gray-600 whitespace-pre-wrap">
                    {actionData.result}
                  </p>
                </div>
                <Button
                  onClick={() => {
                    formRef.current?.reset();
                    window.location.reload();
                  }}
                  className="text-blue-600 hover:text-blue-700"
                  variant="link"
                >
                  Analyze another case
                </Button>
              </div>
            )}

            <div className="bg-white/70 backdrop-blur-sm rounded-lg border border-gray-300 p-6 shadow-lg">
              <div className="flex items-start space-x-4">
                <div className="bg-blue-100 rounded-full p-2">
                  <Info className="h-5 w-5 text-blue-600" />
                </div>
                <div className="text-left">
                  <h3 className="text-lg font-semibold text-gray-800 mb-2">
                    For the most accurate assessment
                  </h3>
                  <p className="text-gray-600 leading-relaxed">
                    Please include your pet&apos;s age, weight, and breed, along
                    with any relevant medical history. Mention recent changes in
                    behavior, eating habits, or daily routine. The more detailed
                    information you provide, the better we can help assess your
                    pet&apos;s condition.
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
