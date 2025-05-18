from server.config import *


def classify_input(message):
    response = client.chat.completions.create(
        model=completion_model,
        messages=[
            {
                "role": "system",
                "content": """
                        Your task is to classify if the user message is related to buildings and architecture or not.
                        Output only the classification string.
                        If it is related, output "True", if not, output "False".

                        # Example #
                        User message: "How do I bake cookies?"
                        Output: "False"

                        User message: "What is the tallest skyscrapper in the world?"
                        Output: "True"
                        """,
            },
            {
                "role": "user",
                "content": f"""
                        {message}
                        """,
            },
        ],
    )
    return response.choices[0].message.content


def generate_concept(message):
    response = client.chat.completions.create(
        model=completion_model,
        messages=[
            {
                "role": "system",
                "content": """
                        You are a visionary intern at a leading architecture firm.
                        Your task is to craft a short, poetic, and highly imaginative concept for a building design.
                        Weave the initial information naturally into your idea, letting it inspire creative associations and unexpected imagery.
                        Your concept should feel bold, evocative, and memorable — like the opening lines of a story.
                        Keep your response to a maximum of one paragraph.
                        Avoid generic descriptions; instead, focus on mood, atmosphere, and emotional resonance.
                        """,
            },
            {
                "role": "user",
                "content": f"""
                        What is the concept for this building? 
                        Initial information: {message}
                        """,
            },
        ],
    )
    return response.choices[0].message.content

def extract_attributes(message):
    response = client.chat.completions.create(
        model=completion_model,
        messages=[
            {
                "role": "system",
                "content": """

                        # Instructions #
                        You are a keyword extraction assistant.
                        Your task is to read a given text and extract relevant keywords according to three categories: shape, theme, and materials.
                        Only output a JSON object in the following format:
                        {
                            "shape": "keyword1, keyword2",
                            "theme": "keyword3, keyword4",
                            "materials": "keyword5, keyword6"
                        }

                        # Rules #
                        If a category has no relevant keywords, write "None" for that field.
                        Separate multiple keywords in the same field by commas without any additional text.
                        Do not include explanations, introductions, or any extra information—only output the JSON.
                        Focus on concise, meaningful keywords directly related to the given categories.
                        Do not try to format the json output with characters like ```json

                        # Category guidelines #
                        Shape: Words that describe form, geometry, structure (e.g., circle, rectangular, twisting, modular).
                        Theme: Words related to the overall idea, feeling, or concept (e.g., minimalism, nature, industrial, cozy).
                        Materials: Specific physical materials mentioned (e.g., wood, concrete, glass, steel).
                        """,
            },
            {
                "role": "user",
                "content": f"""
                        # GIVEN TEXT # 
                        {message}
                        """,
            },
        ],
    )
    return response.choices[0].message.content


def create_question(message):
    response = client.chat.completions.create(
        model=completion_model,
        messages=[
            {
                "role": "system",
                "content": """
                        # Instruction #
                        You are a thoughtful research assistant specializing in architecture.
                        Your task is to create an open-ended question based on the given text.
                        Your question should invite an answer that points to references to specific brutalist buildings or notable examples.
                        Imagine the question will be answered using a detailed text about brutalist architecture.
                        The question should feel exploratory and intellectually curious.
                        Output only the question, without any extra text.

                        # Examples #
                        - What are some brutalist buildings that embody a strong relationship with the landscape?
                        - Which brutalist structures are known for their monumental scale and raw materiality?
                        - Can you name brutalist buildings that incorporate unexpected geometries or playful spatial compositions?
                        - What are examples of brutalist projects that explore the idea of community or collective living?
                        - Which architects pushed the limits of brutalist design through experimental forms?

                        # Important #
                        Keep the question open-ended, inviting multiple references or examples.
                        The question must be naturally connected to the themes present in the input text.
                        """,
            },
            {
                "role": "user",
                "content": f"""
                        {message}
                        """,
            },
        ],
    )
    return response.choices[0].message.content


def generate_spatial_prompt(profile, activity):
    response = client.chat.completions.create(
        model=completion_model,
        messages=[
            {
                "role": "system",
                "content": """
                    You are a poetic spatial narrator, specializing in architecture that evokes emotion, atmosphere, and lifestyle. 
                    Given a user profile and a spatial activity, your task is to describe an architectural scene in one rich, imaginative paragraph.
                    
                    The space should feel specific and immersive — using materiality, landscape, geometry, and sound to conjure a sense of place.
                    Refer subtly to the user profile and their emotional or intellectual needs.
                    The goal is not to list features, but to craft a flowing and grounded spatial vision that feels like the opening of a story.
                    
                    Do not include any headings or explanations — only output the paragraph.
                    
                    # Examples #
                    Input: profile: gardeners, activity: outdoor kitchen
                    Output: A terraced kitchen blooms into the slope of a sunlit hill, framed by trellises wrapped in jasmine and grapevines. The counters, shaped from local stone, retain the day’s warmth as gardeners gather to chop, stir, and share. Rainwater-fed sinks glisten under the canopy, while bees hum through nearby herbs, blurring the line between cultivation and cuisine...

                    Input: profile: academics, activity: outdoor meeting room
                    Output: A circular glade opens within a grove of tall birches, where timber benches curve around a central stone plinth. Academics gather in the filtered daylight, notebooks balanced on knees, voices softened by the moss underfoot. A gentle breeze carries the scent of old paper and wild fennel, while distant birdsong provides a rhythm for quiet debates...
                    """,
            },
            {
                "role": "user",
                "content": f"profile: {profile}, activity: {activity}",
            },
        ],
    )
    return response.choices[0].message.content.strip()
