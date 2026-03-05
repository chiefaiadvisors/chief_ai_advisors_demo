"""
Chief AI Advisors Animated Demo
Fun and professional simulation of AI-assisted workflows and services.
Author: Tristan Becker
Company: Chief AI Advisors
Website: https://chiefaiadvisors.com
Toll-Free: +1-833-313-7714
Email: chiefaiadvisors@gmail.com
"""
import time
import os

# ----------------------
# Guy Poses — WITH glasses
# ----------------------
GUY_LEFT  = "   (⌐■_■)\n   <)   )╯\n   /    \\"
GUY_RIGHT = "   (⌐■_■)\n    /)  )>\n   /    \\"
GUY_ARMS  = "   (⌐■_■)\n   \\(   )/\n   /    \\"
GUY_CHEER = "  \\(⌐■_■)/\n   |     |\n   /    \\"

# Guy pointing UP with one arm raised (services section)
GUY_POINT_UP_LEFT  = "    \\ (⌐■_■)\n     \\)   )╯\n      /    \\"
GUY_POINT_UP_RIGHT = "   (⌐■_■) /\n   <)   )/ \n   /    \\  "

# ----------------------
# Guy Poses — WITHOUT glasses (SEO section sidekicks)
# ----------------------
NOGLASS_LEFT  = "   (•_•)\n   <)   )╯\n   /    \\"
NOGLASS_RIGHT = "   (•_•)\n    /)  )>\n   /    \\"
NOGLASS_ARMS  = "   (•_•)\n   \\(   )/\n   /    \\"

# ----------------------
# ASCII Phone (contact slide)
# ----------------------
PHONE = [
    r"  .------.",
    r"  |      |",
    r"  | CALL |",
    r"  |  US  |",
    r"  |      |",
    r"  | o  o |",
    r"  |  __  |",
    r"  '------'",
]

# ----------------------
# Helper: print three guys side by side
# ----------------------
def print_three_guys(pose_left, pose_mid, pose_right):
    lines_l = pose_left.split("\n")
    lines_m = pose_mid.split("\n")
    lines_r = pose_right.split("\n")
    height = max(len(lines_l), len(lines_m), len(lines_r))
    while len(lines_l) < height: lines_l.insert(0, "")
    while len(lines_m) < height: lines_m.insert(0, "")
    while len(lines_r) < height: lines_r.insert(0, "")
    col = 14
    for l, m, r in zip(lines_l, lines_m, lines_r):
        print(f"  {l:<{col}}{m:<{col}}{r}")

# ----------------------
# Build-up Frames — original glasses animation
# ----------------------
build_frames = [
r"""
   (•_•)
   |    |
   /    \
""",
r"""
   (•_•)
   <)   )╯
   /    \
""",
r"""
   (•_•)
  ⌐■-■)
   <)   )╯
   /    \
""",
r"""
   (⌐■_■)
   <)   )╯
   /    \

   Ready for AI workflow!
""",
]

# ----------------------
# Intro Finger Gun Frames
# ----------------------
finger_gun_messages = [
    ("🚀 Launching AI solutions...",      GUY_LEFT),
    ("📊 Data Analytics & Insights",       GUY_RIGHT),
    ("⚖  Compliance & Reporting",          GUY_LEFT),
    ("🌐 SEO & AEO Optimization",          GUY_RIGHT),
    ("🤖 Custom AI Tools & Automation",    GUY_LEFT),
    ("✅ Chief AI Advisors at work!",       GUY_ARMS),
]

# ----------------------
# ASCII Logo — Chief AI Advisors
# Shield with lightbulb + circuit, then company name
# ----------------------
ASCII_LOGO = r"""
                                                        
                           .;;.                         
                        ,;++++++;,                      
                    .:|+==========+|:.                  
                .:|+*****+|;;;;|+*****+|:.              
             :+=*****=*+:::;||;:::+*=*****=+:           
             +?******?;.|*??++??*|.;?******?+           
             |?*****?;.*?*?::::?*?*.;?*****?|           
             |??????+ ?%???,;;,???%? +??????|           
             |%????%:;%|;|?%,,%?|;|%;:%????%|           
             ;%????%,+= *.|&;;&|.* *+,%????%;           
             ;&%%%%&;:%;;.;&;;&:.;;%:;&%%%%&;           
             :&%%%%%? *&%%;::::;%%#* ?%%%%%&:           
             .%&&&&%&* *&&&=  *&&&* *&%&&&&%.           
              ?&&&&&&#* ?&%#;;#%&? *#&&&&&&?            
              ;#&&&&&&#+,#&#;;#&#,+#&&&&&&#;            
               ?#&#####& ?%&::&%? &#####&#?             
               .%#######||||||||||#######&.             
                .%######&========&######%.              
                  *#####&*=****=*&#####*                
                   :&#####|....|#####&:                 
                     |&####*;;*####&|                   
                       |&########&|                     
                         ;%####%;                       
                           :??:                         

      ___  _      _        __     _     ___ 
     / __|| |_   (_) ___  / _|   /_\   |_ _|
    | (__ | ' \  | |/ -_)|  _|  / _ \   | | 
     \___||_||_| |_|\___||_|   /_/ \_\ |___|

   /\   |~\   \  /  [=]    /~~  /~~\  |~~\   /~~ 
  /  \  |  |   \/    |     \__  |  |  |__/   \__ 
  /--\  |  |   \/    |       )  |  |  |\ \     )  
  /  \  |__/   \/   [=]    \__/ \__/  |  \   \__/
"""

# ----------------------
# Services list
# ----------------------
services = [
    ("🤖", "Custom AI Tools & Automation",            GUY_RIGHT),
    ("📊", "Data Analytics & Insights",                GUY_LEFT),
    ("⚖ ", "Compliance & Reporting",                   GUY_RIGHT),
    ("🌐", "SEO & AEO Optimization",                   GUY_LEFT),
    ("💼", "Workflow Optimization & Client Solutions",  GUY_RIGHT),
    ("🛠 ", "IT & AI Integrations",                    GUY_LEFT),
    ("📈", "Business Intelligence & Strategy",         GUY_RIGHT),
    ("🔒", "Data Security & Privacy Management",       GUY_LEFT),
]

# ----------------------
# SEO Spotlight
# (icon, title, detail, main-guy-pose, left-noglass-pose, right-noglass-pose)
# ----------------------
seo_highlights = [
    ("🔍", "SEO Optimization",
     "Rank higher on Google with AI-driven keyword strategy,\n               on-page fixes & backlink analysis.",
     GUY_RIGHT, NOGLASS_LEFT, NOGLASS_ARMS),
    ("🤖", "AEO Optimization",
     "Get featured in AI answer engines (ChatGPT, Perplexity,\n               Gemini) with structured content.",
     GUY_LEFT, NOGLASS_ARMS, NOGLASS_RIGHT),
    ("📈", "Traffic Growth",
     "Drive qualified visitors through organic search, content\n               marketing & conversion optimization.",
     GUY_RIGHT, NOGLASS_LEFT, NOGLASS_ARMS),
    ("🏆", "Competitive Analysis",
     "Identify gaps vs. competitors and capitalize on\n               untapped ranking opportunities.",
     GUY_LEFT, NOGLASS_ARMS, NOGLASS_RIGHT),
    ("📊", "Performance Reporting",
     "Monthly dashboards: traffic, rankings, impressions\n               & ROI — all in plain English.",
     GUY_RIGHT, NOGLASS_LEFT, NOGLASS_RIGHT),
]

# ----------------------
# Workflow Steps
# ----------------------
workflow_steps = [
    ("Receive client data",                                    "📥", GUY_LEFT),
    ("Validate data completeness",                             "🔎", GUY_RIGHT),
    ("Log into CRM",                                           "💻", GUY_LEFT),
    ("Upload documents",                                       "📂", GUY_RIGHT),
    ("Run automated quality checks",                           "⚙️ ", GUY_LEFT),
    ("Audit website SEO & AEO performance",                    "🔍", GUY_RIGHT),
    ("Optimize content for search & AI answer engines",        "✍️ ", GUY_LEFT),
    ("Implement keyword strategy to boost organic traffic",    "📈", GUY_RIGHT),
    ("Deploy structured data markup for AEO visibility",       "🏗️ ", GUY_LEFT),
    ("Track traffic growth & generate performance report",     "📊", GUY_RIGHT),
    ("Notify team of completion",                              "🔔", GUY_LEFT),
    ("Archive workflow log",                                   "🗄️ ", GUY_RIGHT),
    ("Send final report to stakeholders",                      "📧", GUY_CHEER),
]

# ----------------------
# Robot Frames
# Frame A: [WORK] DOWN (starts here), cactus arms UP
# Frame B: [WORK] UP,  cactus arms FLAT
# ----------------------
ROBOT_WORK_DOWN = [
    r"                   ",
    r"  ¤  [=====]       ",
    r"     |v . v|       ",
    r"  ^  | ___ |  ^    ",
    r"  |  |_____|  |    ",
    r"       |           ",
    r"     [WORK]        ",
    r"     _____         ",
]

ROBOT_WORK_UP = [
    r"     [WORK]        ",
    r"       |           ",
    r"  ¤  [=====]       ",
    r"     |^ . ^|       ",
    r"  ---| ___ |---    ",
    r"  |  |_____|  |    ",
    r"      || ||        ",
    r"     _|| ||_       ",
]

# Starts DOWN so first move is lifting UP
ROBOT_FRAMES = [ROBOT_WORK_DOWN, ROBOT_WORK_UP]

# ----------------------
# Helper Functions
# ----------------------
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause(prompt="Press Enter to continue..."):
    input(f"\n  {prompt}")

def print_guy(pose):
    for line in pose.split("\n"):
        print("  " + line)

def animate_build(frames, delay=0.75):
    for frame in frames:
        clear()
        print(frame)
        time.sleep(delay)

def animate_finger_guns(gun_frames, delay=1.1):
    for message, pose in gun_frames:
        clear()
        print()
        print_guy(pose)
        print(f"\n   {message}")
        time.sleep(delay)

def print_guy_and_robot(guy_pose, robot_frame):
    """Guy (left) side-by-side with robot (right), feet aligned."""
    guy_lines = guy_pose.split("\n")
    while len(guy_lines) < len(robot_frame):
        guy_lines.insert(0, "")
    guy_col = 18
    for g, r in zip(guy_lines, robot_frame):
        print(f"  {g:<{guy_col}}{r}")

# ----------------------
# ASCII Computer (services section)
# ----------------------
COMPUTER = [
    r" .------------------.",
    r" |  ______________ |",
    r" | |              | |",
    r" | |   CHIEF AI   | |",
    r" | |   ADVISORS   | |",
    r" | |______________| |",
    r" |__________________|",
    r"   |     ______    |",
    r"   |____|______|___|",
    r"   ~~~~~~~~~~~~~~~~~ ",
]

def render_services_scene(printed_services, guy_pose, position="left"):
    STAGE_WIDTH = 58
    comp_col_width = 22
    print("\n" + "="*STAGE_WIDTH)
    print("   🌟  Chief AI Advisors — Our Services  🌟")
    print("="*STAGE_WIDTH + "\n")
    right_lines = printed_services
    n_rows = max(len(COMPUTER), len(right_lines))
    comp_padded  = COMPUTER + [""] * (n_rows - len(COMPUTER))
    right_padded = [""] * (n_rows - len(right_lines)) + right_lines
    for c, r in zip(comp_padded, right_padded):
        print(f"  {c:<{comp_col_width}}  {r}")
    print()
    guy_lines = guy_pose.split("\n")
    indent_left  = " " * 2
    indent_right = " " * (comp_col_width + 6)
    indent = indent_right if position == "right" else indent_left
    for line in guy_lines:
        print(indent + line)

# ----------------------
# Services Screen
# ----------------------
def display_services():
    printed = []
    positions = ["left", "right"] * 8

    for i, (icon, service, _) in enumerate(services):
        pos = positions[i]
        pose = GUY_POINT_UP_RIGHT if pos == "right" else GUY_POINT_UP_LEFT
        midpos = "left" if pos == "right" else "right"
        for walk_pos, walk_pose in [(midpos, GUY_ARMS), (pos, pose)]:
            clear()
            render_services_scene(printed, walk_pose, position=walk_pos)
            time.sleep(0.3)
        new_line = f"  {icon}  {service}"
        printed.append(new_line)
        clear()
        render_services_scene(printed, pose, position=pos)
        time.sleep(0.9)

    # Final frame
    clear()
    print("\n" + "="*58)
    print("   🌟  Chief AI Advisors — Our Services  🌟")
    print("="*58 + "\n")
    n_rows = max(len(COMPUTER), len(printed))
    comp_padded  = COMPUTER + [""] * (n_rows - len(COMPUTER))
    right_padded = [""] * (n_rows - len(printed)) + printed
    for c, r in zip(comp_padded, right_padded):
        print(f"  {c:<22}  {r}")
    print()
    cheer_lines = GUY_CHEER.split("\n")
    for line in cheer_lines:
        print("  " + " " * 14 + line)
    print("\n  That's what we do. All of it. 💼\n")
    print("-"*58)
    print("  🌐  https://chiefaiadvisors.com")
    print("  📞  +1-833-313-7714")
    print("  📧  chiefaiadvisors@gmail.com")
    print("-"*58)
    pause("Press Enter to see our SEO & AEO approach...")

# ----------------------
# SEO Spotlight Screen  — 3 guys the WHOLE time, line-by-line reveal
# ----------------------
def display_seo_spotlight():
    all_lines = []   # flat list of fully-revealed lines so far

    for icon, title, detail, main_pose, left_pose, right_pose in seo_highlights:
        # Build lines for this entry: title line + each detail word-wrapped line
        entry_lines = [f"  {icon}  {title}"]
        for dl in detail.split("\n"):
            entry_lines.append(f"               {dl.strip()}")
        entry_lines.append("")  # blank spacer after each entry

        # Reveal this entry one line at a time
        for li, new_line in enumerate(entry_lines):
            clear()
            print("\n" + "="*58)
            print("   🌐  SEO, AEO & Customer Traffic Growth  🌐")
            print("="*58 + "\n")
            # Print all previously completed entries
            for l in all_lines:
                print(l)
            # Print the lines of the current entry revealed so far
            for l in entry_lines[:li+1]:
                print(l)
            print()
            # Alternate guy poses as lines come in
            tick = (len(all_lines) + li) % 2
            lp = left_pose  if tick == 0 else NOGLASS_ARMS
            rp = right_pose if tick == 0 else NOGLASS_ARMS
            print_three_guys(lp, main_pose, rp)
            time.sleep(0.22)

        # Commit this entry to the permanent list
        all_lines.extend(entry_lines)

    # Final frame — everything shown, all 3 guys cheering
    clear()
    print("\n" + "="*58)
    print("   🌐  SEO, AEO & Customer Traffic Growth  🌐")
    print("="*58 + "\n")
    for l in all_lines:
        print(l)
    print_three_guys(NOGLASS_LEFT, GUY_CHEER, NOGLASS_RIGHT)
    print("\n  Your competitors aren't waiting. Neither should you. 🚀\n")
    print("-"*58)
    print("  🌐  https://chiefaiadvisors.com")
    print("  📞  +1-833-313-7714")
    print("  📧  chiefaiadvisors@gmail.com")
    print("-"*58)
    pause("Press Enter to see our AI workflow in action...")

# ----------------------
# Workflow Screen — one guy with glasses + robot
# ----------------------
def run_workflow(steps):
    printed = []
    robot_tick = 0  # starts at 0 = WORK DOWN, first step lifts UP

    for i, (step, icon, main_pose) in enumerate(steps, start=1):
        robot_frame = ROBOT_FRAMES[robot_tick % 2]
        robot_tick += 1

        clear()
        print("\n" + "="*58)
        print("   🤖  AI-Assisted Workflow Simulation")
        print("="*58 + "\n")
        for prev in printed:
            print(prev)
        print()
        print_guy_and_robot(main_pose, robot_frame)
        new_line = f"  Step {i:>2}/{len(steps)}: {icon} {step} ✅"
        print(f"\n  >>> Step {i}: {step}")
        printed.append(new_line)
        time.sleep(0.9)

    # Final frame — all steps, guy cheering + robot WORK UP
    clear()
    print("\n" + "="*58)
    print("   🤖  AI-Assisted Workflow Simulation")
    print("="*58 + "\n")
    for line in printed:
        print(line)
    print()
    print_guy_and_robot(GUY_CHEER, ROBOT_WORK_UP)
    print("\n  All done. Smooth as butter. 🧈\n")
    print("-"*58)
    print("  All workflow steps executed with AI oversight.")
    print("-"*58)
    print("  🌐  https://chiefaiadvisors.com")
    print("  📞  +1-833-313-7714")
    print("  📧  chiefaiadvisors@gmail.com")
    print("-"*58)
    pause("Press Enter to see the workflow summary...")

# ----------------------
# Summary Screen — one guy with glasses + clipboard
# ----------------------

# ----------------------
# Summary Screen — one guy with glasses + animated clipboard
# ----------------------

CLIPBOARD_ROWS = 4  # checkable rows on the clipboard

def build_clipboard(checked):
    """Return clipboard lines with `checked` boxes ticked."""
    rows = [
        r"   _________  ",
        r"  |  ___    | ",
        r"  | |___|   | ",
        r"  |         | ",
    ]
    for i in range(CLIPBOARD_ROWS):
        tick = "[+]" if i < checked else "[ ]"
        rows.append(f"  | {tick} ... | ")
    rows.append(r"  |_________| ")
    return rows

def print_guy_and_clipboard(guy_pose, clipboard):
    guy_lines = guy_pose.split("\n")
    while len(guy_lines) < len(clipboard):
        guy_lines.insert(0, "")
    col = 18
    for g, c in zip(guy_lines, clipboard):
        print(f"  {g:<{col}}{c}")

def summary(steps):
    total = len(steps)
    # Tick one box per quarter of steps completed
    quarter = total / CLIPBOARD_ROWS
    checked = 0

    for i, (step, icon, _) in enumerate(steps):
        # Check if we've crossed into the next quarter
        new_checked = int(i / quarter) if quarter > 0 else 0
        if new_checked > checked:
            checked = new_checked

        clear()
        print("\n" + "="*58)
        print("   📋  Workflow Summary")
        print("="*58 + "\n")
        print_guy_and_clipboard(GUY_RIGHT, build_clipboard(checked))
        print()
        for j, (s, ic, _) in enumerate(steps[:i+1]):
            print(f"  {j+1:>2}. {ic} {s} ✔")
        time.sleep(0.25)

    # Final frame — all boxes ticked, guy cheering
    clear()
    print("\n" + "="*58)
    print("   📋  Workflow Summary")
    print("="*58 + "\n")
    print_guy_and_clipboard(GUY_CHEER, build_clipboard(CLIPBOARD_ROWS))
    print()
    for i, (step, icon, _) in enumerate(steps):
        print(f"  {i+1:>2}. {icon} {step} ✔")
    print("\n" + "-"*58)
    print(f"  Total steps : {total}")
    print(f"  Status      : All completed successfully ✅")
    print("-"*58)
    print("  🌐  https://chiefaiadvisors.com")
    print("  📞  +1-833-313-7714")
    print("  📧  chiefaiadvisors@gmail.com")
    print("-"*58)
    pause("Press Enter to see contact info...")

# ----------------------
# Contact Slide — phone rings back and forth
# ----------------------

PHONE_QUIET = [
    r"   .------.",
    r"   |      |",
    r"   | CALL |",
    r"   |  US  |",
    r"   |      |",
    r"   | o  o |",
    r"   |  __  |",
    r"   '------'",
]

PHONE_RING = [
    r"~~ .------. ~~",
    r"   |      |   ",
    r"   | CALL |   ",
    r"   |  US  |   ",
    r"   |      |   ",
    r"   | o  o |   ",
    r"   |  __  |   ",
    r"   '------'   ",
]

def display_contact():
    speech = [
        " _____________________",
        "| Hey! Contact us!    |",
        "| We'd love to chat!  |",
        "|_____________________|",
        "        \\",
        "",
        "",
        "",
    ]
    col_speech = 26
    col_guy    = 18

    def render_contact(phone_frame):
        clear()
        print("\n" + "="*58)
        print("   📞  Get In Touch With Chief AI Advisors  📞")
        print("="*58 + "\n")
        guy_lines = GUY_RIGHT.split("\n")
        while len(guy_lines) < len(phone_frame):
            guy_lines.insert(0, "")
        sp = speech + [""] * (len(phone_frame) - len(speech))
        for s, g, p in zip(sp, guy_lines, phone_frame):
            print(f"  {s:<{col_speech}}{g:<{col_guy}}{p}")
        print("\n" + "-"*58)
        print("  🌐  Website  :  https://chiefaiadvisors.com")
        print("  📞  Phone    :  +1-833-313-7714")
        print("  📧  Email    :  chiefaiadvisors@gmail.com")
        print("-"*58)
        print("\n  Tristan Becker | Chief AI Advisors")
        print("  Helping businesses grow with AI — one step at a time. 🚀\n")

    # Ring animation — 4 rings
    for _ in range(4):
        render_contact(PHONE_RING)
        time.sleep(0.4)
        render_contact(PHONE_QUIET)
        time.sleep(0.3)

    # Hold on ringing
    render_contact(PHONE_RING)
    pause("Press Enter — we'll pick up on the first ring ☎️ ...")

# ----------------------
# Main Execution
# ----------------------
if __name__ == "__main__":

    # 1. Character build-up
    animate_build(build_frames, delay=0.75)

    # 2. Intro finger gun teaser
    animate_finger_guns(finger_gun_messages, delay=1.1)

    # Transition — mission statement then Enter
    clear()
    print_guy(GUY_ARMS)
    print("\n  💼 Chief AI Advisors — Let's get to work!\n")
    print("  " + "─"*54)
    print()
    print("  We establish your authority in an AI-driven search")
    print("  world — so your business becomes visible, trusted,")
    print("  and chosen.")
    print()
    print("  We don't promise 10x results or revolutionary")
    print("  breakthroughs. We build durable foundations that")
    print("  compound over time. Substance over sizzle, always.")
    print()
    print("  Most agencies sell you one layer of the stack.")
    print("  We architect the entire system.")
    print()
    print("  " + "─"*54)
    pause("Press Enter to see what we offer...")

    # 3. Services — value proposition
    display_services()

    # 4. SEO/AEO Spotlight — key differentiator
    display_seo_spotlight()

    # 5. Workflow — proof of process
    run_workflow(workflow_steps)

    # 6. Summary — close the loop
    summary(workflow_steps)

    # 7. Contact slide
    display_contact()

    # 8. Logo outro
    clear()
    print(ASCII_LOGO)
    print("  " + "─"*44)
    print("  Tristan Becker & Yvonne Becker | Chief AI Advisors")
    print("  🌐  https://chiefaiadvisors.com")
    print("  📞  +1-833-313-7714")
    print("  📧  chiefaiadvisors@gmail.com")
    print("  " + "─"*44)
    pause("Press Enter to exit — let's teach your website to work a little harder for you. 💡")
