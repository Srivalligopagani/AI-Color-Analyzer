import pymiere
import os

def connect_to_premiere():
    """
    Forcefully attempts to find the active Premiere Pro process 
    and returns the project object.
    """
    try:
        # Check if Premiere is even running
        project = pymiere.objects.app.project
        if project:
            print(f"✅ Success! Connected to: {project.name}")
            return project
    except Exception as e:
        print(f"❌ Connection Failed: {e}")
        return None

def apply_color_vibe(r, g, b):
    project = connect_to_premiere()
    if not project:
        return "Lagging: Premiere Pro not responding. Check 'Allow Scripts' setting."

    # This is the 'Secret Sauce': Manual property injection
    # We target the active sequence and the first clip
    active_seq = project.activeSequence
    clip = active_seq.videoTracks[0].clips[0]
    
    # Targeting Lumetri Color component directly
    for comp in clip.components:
        if "Lumetri" in comp.displayName:
            # Adobe 2022 uses decimal values (0.0 to 1.0)
            # We divide your 0-255 colors by 255
            shadow_tint = [r/255.0, g/255.0, b/255.0, 1] 
            comp.properties[10].setValue(shadow_tint)
            return True
    return "Lumetri Color effect not found on clip! Add it manually first."