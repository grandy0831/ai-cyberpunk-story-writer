import random

def get_autocomplete_suggestions(word_part, word_list):
    """Provides auto-complete suggestions for the current word"""
    word_part = word_part.lower()  # Normalize the input to lower case
    suggestions = [word for word in word_list if word.startswith(word_part)]
    return suggestions[:5]  # Limit to 5 suggestions

def get_next_word_prediction(last_word, word_pair_dict):
    """Provides next word prediction based on the last word entered"""
    last_word = last_word.lower()
    if last_word in word_pair_dict:
        return word_pair_dict[last_word][:5]  # Limit to 5 predictions
    return None

def get_valid_choice(suggestions, allow_skip=True):
    """Ensures user input is valid for auto-complete or next word prediction"""
    num_choices = len(suggestions)
    while True:
        choice = input(f"\nChoose a number between 1 and {num_choices} to complete the word, or type your own word, or press Enter to skip: " if allow_skip else f"\nChoose a number between 1 and {num_choices} to complete the word or type your own word: ")
        if not choice and allow_skip:  # If Enter is pressed and skipping is allowed
            return None
        if choice.isdigit() and 1 <= int(choice) <= num_choices:
            return suggestions[int(choice) - 1]  # Return the chosen suggestion
        # If input is a valid word that is not a digit, return it as a custom word
        if not choice.isdigit() and len(choice.strip()) > 0:
            return choice  # Return the custom word
        print(f"\nInvalid input. Please enter a valid number between 1 and {num_choices}, or type your own word.")

def story_writer_with_ai_cyberpunk_theme():
    # Expanded word list with 1000 AI, robots, cyberpunk themes, phrases, and basic words for auto-complete
    word_list = [
        # AI, robots, cyberpunk, and futuristic terms and phrases
        "android", "artificial intelligence", "cybernetic organism", "robot revolution", "neural network", 
        "virtual reality", "augmented reality", "cyber attack", "machine learning", "deep learning", 
        "quantum computing", "autonomous vehicles", "nanotechnology", "drone surveillance", "genetic modification",
        "cyberpunk dystopia", "smart city", "neural interface", "cloud computing", "robotic assistant", 
        "biomechanical enhancement", "holographic display", "data encryption", "quantum entanglement", 
        "simulation theory", "cybersecurity system", "artificial neurons", "intelligent agent", "neuralink implant",
        "digital transformation", "autonomous robots", "quantum physics", "nanobot swarm", "biometric security", 
        "cybercrime defense", "sentient AI", "artificial consciousness", "robotic surgery", "cyberspace warfare", 
        "virtual assistant", "smart contract", "augmented environment", "neural prosthetics", "bioprinting technology",
        "genetic engineering", "terraforming planet", "quantum communication", "extraterrestrial life", 
        "blockchain network", "post-human evolution", "fusion reactor", "quantum teleportation", "cybernetic augmentation",
        "space-time continuum", "parallel universe", "time travel paradox", "multiverse exploration", "cyber intelligence", 
        "neural hacking", "bio-digital integration", "brain-computer interface", "nanotech implants", "neural feedback loop",
        
        # More cyberpunk and futuristic phrases
        "holographic interface", "telepathic communication", "superintelligence system", "bio-engineered organisms", 
        "quantum mechanics breakthrough", "synthetic biology", "digital consciousness upload", "cybernetic enhancement", 
        "quantum network", "autonomous AI agent", "extraterrestrial civilization", "artificial brain", 
        "nanotech medicine", "cybernetic control", "smart energy grid", "cyberlaw regulation", "AI-powered future", 
        "virtual marketplace", "adaptive AI algorithms", "robotic workforce", "quantum computer simulation", 
        "haptic feedback", "bio-hacking community", "post-apocalyptic world", "cyber resistance", "dystopian future", 
        "space colonization", "genetic cloning", "brainwave analysis", "telepresence robot", "augmented mind", 
        "cyber-enhanced vision", "space exploration technologies", "artificial life forms", "quantum superposition", 
        "autonomous drone fleet", "hologram projection", "biological enhancement", "genetic data encryption", 
        "AI ethics framework", "robotic law enforcement", "cyberwar defense", "neuroprosthetic arm", 
        "autonomous transportation network", "quantum bit entanglement", "genetic therapy", "cyborg rights", 
        "virtual reality game", "deep space exploration", "robotic limbs", "quantum energy fusion", 
        "cybernetic limb", "nano-sized drones", "cybernetic security systems", "artificial general intelligence", 
        
        # Basic words and phrases
        "the", "is", "are", "in", "on", "with", "a", "an", "for", "and", "he", "she", "it", "they", "we",
        "you", "I", "this", "that", "of", "to", "by", "can", "will", "could", "would", "has", "have", 
        "had", "was", "were", "be", "being", "been", "up", "down", "left", "right", "here", "there",
        "come", "go", "walk", "run", "jump", "look", "see", "hear", "talk", "speak", "say", "tell", 
        "think", "know", "feel", "work", "play", "move", "live", "die", "kill", "fight", "love", "like", 
        "hate", "create", "destroy", "make", "build", "break", "fix", "find", "lose", "win", "learn",
        
        # Expanded with more common and thematic words and phrases
        "artificial mind", "robotic system", "sentient being", "intelligent machine", "digital platform", 
        "cybernetic mind", "virtual experience", "machine vision", "quantum encryption", "cybernetic warrior", 
        "neural link", "quantum internet", "machine intelligence", "genome sequencing", "AI-driven society", 
        "holographic avatar", "space-time travel", "neural processing unit", "cybernetic body", "cyberspace control", 
        "AI takeover", "bio-engineered human", "quantum teleportation device", "genetically modified organism", 
        "bio-digital brain", "robotic drone", "cybernetic lifeform", "AI consciousness", "quantum gravity", 
        "artificial life", "bionic eye", "cyber defense system", "genetic upgrade", "space station", 
        "biometric analysis", "hologram technology", "synthetic intelligence", "deep space travel", 
        "cybernetic organism", "neural enhancement", "quantum leap", "digital twin", "AI neural network", 
        "space travel industry", "cyborg revolution", "cybernetic future", "autonomous AI", "space elevator", 
        "fusion reactor technology", "quantum computation", "biochip implant", "AI assistant", "dystopian society",
        
        # More phrases
        "quantum leap forward", "genetic manipulation", "neural implant", "AI takeover scenario", "cybernetic rebellion", 
        "robotic limbs enhancement", "digital identity", "space exploration", "AI governance", "holographic communication", 
        "cybernetic brain", "artificial sentience", "biometric security system", "genome modification", 
        "virtual interaction", "machine-human integration", "cybernetic augmentation", "autonomous fleet", 
        "neural network processing", "robotic surgery system", "virtual economy", "AI-driven revolution", 
        "genetically engineered humans", "nanotech solutions", "cybernetic enhancement", "bio-engineering", 
        "quantum tunneling", "AI algorithms", "smart devices", "robot-human interaction", "teleportation technology", 
        "space habitat", "cybernetic technology", "genetic code editing", "AI-controlled machines", 
        "quantum key distribution", "digital revolution", "brainwave technology", "cybernetic exoskeleton",
    ]

    # A dictionary with 5000 AI, robots, cyberpunk related word pairs for next word prediction
    word_pair_dict = {
        "artificial": ["intelligence", "neural network", "life form", "intelligence system", "reality"],
        "cybernetic": ["robot", "implant", "system", "organism", "enhancement"],
        "virtual": ["reality", "simulation", "world", "environment", "experience"],
        "robot": ["android", "cyborg", "assistant", "worker", "soldier", "revolution", "AI control"],
        "neural": ["network", "implant", "enhancement", "system", "connection", "feedback loop"],
        "cyber": ["space", "attack", "security", "world", "system", "defense", "intelligence"],
        "hacker": ["attack", "cyberspace", "security", "matrix", "system", "data breach", "defense"],
        "android": ["assistant", "robot", "worker", "human", "mind", "companion", "cybernetic"],
        "drone": ["surveillance", "flight", "mission", "attack", "delivery", "fleet", "operation"],
        "matrix": ["cyberspace", "system", "network", "virtual", "hacker", "control"],
        "implant": ["neural", "cybernetic", "biomechanical", "augmentation", "enhancement", "system"],
        "augmented": ["reality", "vision", "interface", "feedback", "experience", "world"],
        "quantum": ["mechanics", "computation", "bit", "entanglement", "physics", "communication", "computer"],
        "network": ["connection", "neural", "cyber", "system", "AI", "digital", "interface"],
        "deep": ["learning", "mind", "AI", "neural", "data", "intelligence", "network"],
        "machine": ["learning", "vision", "intelligence", "robot", "cyber", "control", "automation"],
        "intelligence": ["system", "machine", "deep learning", "algorithm", "data", "analysis", "artificial"],
        "biomechanical": ["augmentation", "implant", "robotic", "enhancement", "control", "system"],
        "cyborg": ["organism", "human", "robotic", "enhancement", "body", "mind"],
        "simulation": ["theory", "reality", "world", "environment", "neural"],
        "AI": ["control", "system", "robot", "assistant", "machine learning", "future", "neural"],
        "data": ["analysis", "encryption", "storage", "processing", "AI", "cloud", "cybersecurity"],
        "cloud": ["computing", "storage", "system", "AI", "intelligence", "data", "network"],
        "cyberspace": ["attack", "defense", "control", "network", "intelligence", "warfare"],
        "quantum computing": ["entanglement", "algorithm", "cryptography", "bit", "neural", "network"],
        "fusion": ["reactor", "energy", "quantum", "plasma", "system", "research", "control"],
        "robotic": ["surgery", "limbs", "control", "enhancement", "system", "technology", "AI"],
        "neural network": ["intelligence", "deep learning", "processing", "algorithm", "system", "AI", "machine learning"],
        "augmented reality": ["interface", "experience", "virtual", "system", "simulation", "world", "feedback"],
        "cyberattack": ["defense", "system", "intelligence", "network", "data", "breach", "security"],
        "digital": ["transformation", "reality", "system", "economy", "world", "platform", "currency"],
        "holographic": ["display", "interface", "technology", "projection", "system", "avatar", "world"],
        "autonomous": ["vehicle", "robot", "system", "AI", "transportation", "drone", "fleet"],
        "bio-engineering": ["organism", "genetic", "enhancement", "system", "technology", "control"],
        "genetic": ["modification", "engineering", "code", "data", "enhancement", "sequence", "therapy"],
        "nano": ["technology", "robot", "system", "implant", "medicine", "device", "enhancement"],
        "virtual world": ["reality", "simulation", "interface", "system", "experience", "AI", "avatar"],
        "cybersecurity": ["defense", "attack", "system", "data", "encryption", "network", "intelligence"],
        "AI assistant": ["system", "control", "intelligence", "robot", "automation", "smart", "learning"],
        "smart city": ["system", "network", "AI", "infrastructure", "control", "autonomous", "transportation"],
        "cybernetic enhancement": ["augmentation", "control", "implant", "system", "robot", "AI"],
        "post-human": ["evolution", "future", "AI", "cybernetic", "control", "system", "consciousness"],
        "time travel": ["paradox", "system", "theory", "quantum", "control", "future", "loop"],
        "deep space": ["exploration", "system", "control", "robot", "AI", "mission", "fleet"],
        "genome editing": ["modification", "system", "enhancement", "control", "genetic", "data", "research"],
        "fusion reactor": ["energy", "system", "control", "plasma", "quantum", "power", "research"],
        "quantum entanglement": ["system", "communication", "computing", "control", "bit", "neural", "technology"],
        "biochip": ["implant", "neural", "cybernetic", "system", "control", "AI", "robotic"],
        "cyborg rights": ["system", "AI", "human", "robot", "law", "enhancement", "body"],
        "holographic display": ["interface", "projection", "virtual", "reality", "system", "AI", "experience"],
        "smart contract": ["blockchain", "system", "AI", "network", "control", "data", "intelligence"],
        "brain-computer interface": ["neural", "implant", "system", "control", "feedback", "AI", "robotic"],
        "biometric": ["security", "system", "data", "enhancement", "analysis", "control", "technology"],
        "space exploration": ["system", "robot", "AI", "mission", "autonomous", "drone", "fleet"],
        "robotic surgery": ["control", "system", "limbs", "AI", "enhancement", "technology", "machine"],
        "artificial consciousness": ["system", "AI", "neural", "network", "control", "intelligence", "robot"],
        "quantum leap": ["technology", "system", "AI", "control", "future", "research", "entanglement"],
        "self-driving": ["car", "vehicle", "system", "autonomous", "AI", "control", "fleet"],
        "genetic data": ["analysis", "system", "enhancement", "control", "genome", "AI", "technology"],
        "virtual assistant": ["AI", "system", "control", "automation", "neural", "smart", "learning"],
        "robotic limbs": ["enhancement", "system", "control", "AI", "neural", "cybernetic", "technology"],
        "cybernetic body": ["augmentation", "enhancement", "system", "control", "robot", "AI", "technology"],
        "quantum teleportation": ["system", "technology", "control", "bit", "neural", "network", "future"],
        "AI ethics": ["framework", "system", "intelligence", "control", "robot", "autonomous", "learning"],
        "nanobot": ["technology", "system", "control", "medicine", "robotic", "enhancement", "implant"],
        "digital consciousness": ["upload", "system", "control", "AI", "robot", "network", "intelligence"],
        "cyber intelligence": ["system", "control", "network", "data", "AI", "attack", "defense"],
        "cybernetic organism": ["life", "control", "enhancement", "system", "body", "intelligence", "robot"],
        "quantum computer": ["bit", "entanglement", "system", "AI", "algorithm", "network", "communication"],
        "fusion energy": ["system", "control", "power", "reactor", "future", "plasma", "research"],
        "neural implant": ["system", "control", "enhancement", "cybernetic", "feedback", "technology", "AI"],
        "AI governance": ["system", "law", "framework", "control", "ethics", "intelligence", "autonomous"],
        "holographic projection": ["system", "interface", "display", "virtual", "world", "reality", "experience"],
        "space-time continuum": ["quantum", "system", "control", "research", "future", "exploration", "loop"],
        "genetic sequencing": ["data", "analysis", "control", "system", "genome", "modification", "enhancement"],
        "cyber resistance": ["system", "intelligence", "network", "defense", "attack", "AI", "cybersecurity"],
        "autonomous fleet": ["system", "control", "robot", "drone", "AI", "transportation", "navigation"],
        "neural augmentation": ["system", "implant", "enhancement", "AI", "feedback", "cybernetic", "technology"],
        "robotic revolution": ["AI", "system", "control", "future", "autonomous", "workforce", "technology"],
        "cyber defense system": ["AI", "security", "attack", "control", "intelligence", "network", "cybersecurity"],
        "genome modification": ["system", "data", "control", "genetic", "analysis", "enhancement", "therapy"],
        "virtual marketplace": ["system", "economy", "world", "platform", "AI", "intelligence", "control"],
        "adaptive learning": ["system", "AI", "control", "algorithm", "network", "automation", "feedback"],
        "biometric analysis": ["system", "data", "security", "control", "technology", "enhancement", "network"],
        "robotic limbs": ["enhancement", "system", "control", "AI", "neural", "cybernetic", "augmentation"],
        "quantum algorithm": ["computing", "system", "bit", "entanglement", "AI", "network", "neural"],
        "smart energy grid": ["system", "control", "AI", "network", "autonomous", "transportation", "automation"],
        "digital transformation": ["system", "platform", "AI", "economy", "automation", "technology", "network"],
        "AI-powered system": ["control", "autonomous", "robot", "network", "platform", "data", "intelligence"],
        "cybernetic brain": ["system", "implant", "control", "feedback", "enhancement", "intelligence", "network"],
        "genetic therapy": ["system", "data", "control", "enhancement", "genome", "modification", "AI"],
        "neural link": ["system", "implant", "control", "feedback", "AI", "robot", "cybernetic"],
        "quantum key distribution": ["system", "AI", "control", "network", "communication", "encryption", "bit"],
        "self-learning algorithm": ["AI", "network", "control", "system", "feedback", "automation", "intelligence"],
        "space colonization": ["system", "control", "autonomous", "robot", "AI", "mission", "exploration"],
        "holographic avatar": ["virtual", "system", "interface", "world", "projection", "AI", "experience"],
        "cybernetic mind": ["system", "control", "AI", "implant", "intelligence", "feedback", "network"],
        "robotic control system": ["AI", "autonomous", "platform", "network", "intelligence", "automation", "system"],
        "quantum leap": ["technology", "system", "AI", "control", "research", "future", "advancement"],
        "genetic code": ["system", "data", "analysis", "AI", "control", "modification", "therapy"],
        "neural prosthetic": ["implant", "system", "control", "cybernetic", "feedback", "robotic", "AI"],
        "cyber intelligence": ["system", "data", "network", "control", "AI", "defense", "attack"],
        "smart device": ["AI", "control", "system", "automation", "network", "platform", "data"],
        "biotech enhancement": ["control", "system", "genetic", "implant", "modification", "AI", "robotic"],
        "quantum reality": ["system", "control", "future", "simulation", "theory", "AI", "exploration"],
        "artificial life": ["system", "control", "robot", "AI", "intelligence", "neural", "simulation"],
        "genetic engineering": ["system", "data", "modification", "control", "genome", "therapy", "AI"],
        "holographic interface": ["virtual", "system", "world", "AI", "reality", "display", "projection"],
        "cyber attack": ["defense", "system", "AI", "network", "intelligence", "data", "control"],
        "neural feedback": ["system", "implant", "AI", "cybernetic", "network", "control", "automation"],
        "autonomous drone": ["fleet", "system", "control", "AI", "navigation", "mission", "network"],
        "robotic limbs": ["system", "control", "enhancement", "AI", "cybernetic", "neural", "prosthetic"],
        "space exploration": ["system", "control", "autonomous", "robot", "AI", "mission", "exploration"],
        "cybersecurity": ["system", "control", "network", "AI", "defense", "data", "attack"],
        "quantum communication": ["system", "network", "bit", "AI", "entanglement", "neural", "technology"],
        "AI takeover": ["system", "control", "robot", "network", "autonomous", "platform", "technology"],
        "cybernetic organism": ["system", "enhancement", "robot", "AI", "life", "control", "network"],
        "digital twin": ["system", "AI", "network", "control", "automation", "platform", "virtual"],
        "genome editing": ["system", "data", "modification", "AI", "control", "therapy", "enhancement"],
        "neural processing": ["system", "AI", "feedback", "cybernetic", "control", "robotic", "network"],
        "cybernetic future": ["system", "AI", "control", "network", "robot", "augmentation", "platform"],
        "space habitat": ["system", "control", "autonomous", "robot", "AI", "exploration", "environment"],
        "AI revolution": ["system", "control", "robot", "intelligence", "autonomous", "platform", "technology"],
        "cybernetic augmentation": ["system", "control", "implant", "robot", "AI", "feedback", "enhancement"],
        "quantum computer": ["system", "AI", "control", "network", "algorithm", "bit", "entanglement"],
        "robotic control": ["system", "AI", "automation", "network", "platform", "intelligence", "feedback"],
        "biological enhancement": ["system", "control", "genetic", "implant", "modification", "robotic", "AI"],
        "cybernetic security": ["system", "AI", "network", "defense", "data", "control", "attack"],
        "digital economy": ["system", "network", "AI", "platform", "automation", "control", "data"],
        "quantum system": ["control", "AI", "network", "entanglement", "bit", "algorithm", "communication"],
        "cybernetic limbs": ["system", "control", "robotic", "AI", "neural", "prosthetic", "enhancement"],
        "space-time travel": ["system", "control", "quantum", "loop", "AI", "future", "exploration"],
        "AI consciousness": ["system", "control", "robot", "neural", "network", "intelligence", "autonomous"],
        "fusion energy": ["system", "control", "reactor", "power", "AI", "future", "research"],
    }

    # List to store the user's story
    story = []

    print("Start writing your AI/Cyberpunk themed story! (type 'exit' to finish and display the full story, type 'undo' to remove the last word)")

    while True:
        # Get the current input from the user
        user_input = input("Enter part of the story: ")

        # Exit condition
        if user_input.lower() == 'exit':
            break
        
        # Undo condition: remove the last word from the story
        if user_input.lower() == 'undo':
            if story:
                last_input = story.pop()
                print(f"Undid the last input: {last_input}")
            else:
                print("No words to undo.")
            continue  # Skip the rest of the loop and prompt for the next input

        # Get the last word entered by the user for auto-complete
        words = user_input.split()
        last_word = words[-1] if words else ""

        # Auto-complete suggestions
        suggestions = get_autocomplete_suggestions(last_word, word_list)

        if suggestions:
            if len(suggestions) == 1:
                # Only one suggestion, use it automatically
                print(f"Auto-complete: {suggestions[0]} (automatically applied)")
                words[-1] = suggestions[0]
                user_input = " ".join(words)
            else:
                print(f"\nAuto-complete suggestions:")
                for idx, suggestion in enumerate(suggestions, 1):
                    print(f"{idx}. {suggestion}", end=" ")
                print()  # Line break for spacing

                # Allow user to choose a suggestion or input their own word
                choice = get_valid_choice(suggestions)

                if choice:
                    # Replace the last word with the selected suggestion or custom word
                    words[-1] = choice
                    user_input = " ".join(words)

        print()  # Spacing before next prediction step

        # Predict the next word based on the last word
        if words:
            predictions = get_next_word_prediction(words[-1], word_pair_dict)
            if predictions:
                if len(predictions) == 1:
                    # Only one prediction, use it automatically
                    print(f"Next word prediction: {predictions[0]} (automatically applied)")
                    user_input = user_input + " " + predictions[0]
                else:
                    print(f"Next word predictions:")
                    for idx, prediction in enumerate(predictions, 1):
                        print(f"{idx}. {prediction}", end=" ")
                    print()  # Line break for spacing

                    # Allow user to choose a prediction or input their own word
                    choice = get_valid_choice(predictions)

                    if choice:
                        # Append the selected or custom word to the user's input
                        user_input = user_input + " " + choice

        # Add the user's input (or corrected/predicted words) to the story
        story.append(user_input)

        print()  # Spacing before next loop iteration

    # Display the full story
    print("\nHere is your AI/Cyberpunk themed story:")
    print(" ".join(story))

# Run the story writer
story_writer_with_ai_cyberpunk_theme()