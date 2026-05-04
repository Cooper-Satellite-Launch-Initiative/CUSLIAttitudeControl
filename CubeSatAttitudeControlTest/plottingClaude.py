# -*- coding: utf-8 -*-
"""
Created on Mon May  4 14:39:30 2026

@author: Adin Sacho-Tanzer
"""

import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
import pandas as pd

# ============================================================================
# EXAMPLE 1: Detumbling plot with callouts
# ============================================================================

def create_detumbling_plot(detumbling_df):
    """
    Create detumbling plot with callouts showing satellite attitude
    """
    fig = go.Figure()
    
    # Plot the angular velocity data
    fig.add_trace(go.Scatter(
        x=detumbling_df["time.1"]/60,
        y=detumbling_df["Spacecraft Dynamics:4(1)"],
        name="x",
        mode='lines',
        line=dict(color='blue')
    ))
    fig.add_trace(go.Scatter(
        x=detumbling_df["time.1"]/60,
        y=detumbling_df["Spacecraft Dynamics:4(2)"],
        name="y",
        mode='lines',
        line=dict(color='red')
    ))
    fig.add_trace(go.Scatter(
        x=detumbling_df["time.1"]/60,
        y=detumbling_df["Spacecraft Dynamics:4(3)"],
        name="z",
        mode='lines',
        line=dict(color='green')
    ))
    
    # Add reference line
    fig.add_hline(y=1, line_dash="dash", line_color="gray", 
                  annotation_text="1 deg/s", annotation_position="right")
    
    # Add callouts at key points
    # Example: detumbling phase (high angular velocity)
    fig.add_annotation(
        x=30, y=8,
        text="<b>Detumbling Phase</b><br>High spin rate",
        showarrow=True,
        arrowhead=2,
        arrowsize=1,
        arrowwidth=2,
        arrowcolor="red",
        ax=80,
        ay=-60,
        bgcolor="rgba(255, 200, 100, 0.8)",
        bordercolor="red",
        borderwidth=2,
        font=dict(size=12, color="black")
    )
    
    # Example: end of detumbling (low angular velocity)
    fig.add_annotation(
        x=100, y=0.5,
        text="<b>Detumbling Complete</b><br>Spin < 1 deg/s",
        showarrow=True,
        arrowhead=2,
        arrowsize=1,
        arrowwidth=2,
        arrowcolor="green",
        ax=-80,
        ay=-60,
        bgcolor="rgba(150, 255, 150, 0.8)",
        bordercolor="green",
        borderwidth=2,
        font=dict(size=12, color="black")
    )
    
    fig.update_layout(
        title="Detumbling: Angular Velocity About Each Axis",
        xaxis_title="Time (min)",
        yaxis_title="Angular Velocity (deg/s)",
        hovermode='x unified',
        template="plotly_white",
        height=600,
        width=1000,
        showlegend=True,
        legend=dict(x=0.02, y=0.98)
    )
    
    fig.update_xaxes(range=[0, 120])
    fig.update_yaxes(zeroline=True)
    
    return fig


# ============================================================================
# EXAMPLE 2: Nadir pointing with attitude box callouts
# ============================================================================

def create_nadir_plot_with_boxes(nadir_df):
    """
    Create nadir pointing plot with inset boxes showing attitude diagrams
    """
    fig = go.Figure()
    
    # Plot the error data
    time_hours = nadir_df["time"]/3600
    
    fig.add_trace(go.Scatter(
        x=time_hours,
        y=np.rad2deg(nadir_df["Attitude Control:1(1,1)"]),
        name="x error",
        mode='lines',
        line=dict(color='blue')
    ))
    fig.add_trace(go.Scatter(
        x=time_hours,
        y=np.rad2deg(nadir_df["Attitude Control:1(2,1)"]),
        name="y error",
        mode='lines',
        line=dict(color='red')
    ))
    fig.add_trace(go.Scatter(
        x=time_hours,
        y=np.rad2deg(nadir_df["Attitude Control:1(3,1)"]),
        name="z error",
        mode='lines',
        line=dict(color='green')
    ))
    
    # Add reference line
    fig.add_hline(y=8, line_dash="dash", line_color="gray")
    
    # Add callout boxes with descriptions
    # Beginning of nadir pointing
    fig.add_annotation(
        x=2, y=15,
        text="<b>Start of Nadir Pointing</b><br>High initial error",
        showarrow=True,
        arrowhead=2,
        arrowsize=1,
        arrowwidth=2,
        arrowcolor="orange",
        ax=100,
        ay=-80,
        bgcolor="rgba(255, 200, 100, 0.85)",
        bordercolor="orange",
        borderwidth=2,
        font=dict(size=11),
        align="left"
    )
    
    # Convergence phase
    fig.add_annotation(
        x=10, y=6,
        text="<b>Converging to Target</b><br>Error < 8°",
        showarrow=True,
        arrowhead=2,
        arrowsize=1,
        arrowwidth=2,
        arrowcolor="green",
        ax=-120,
        ay=60,
        bgcolor="rgba(150, 255, 150, 0.85)",
        bordercolor="green",
        borderwidth=2,
        font=dict(size=11),
        align="left"
    )
    
    # Steady state
    if len(time_hours) > 15:
        fig.add_annotation(
            x=time_hours.iloc[-1]-2, y=2,
            text="<b>Steady State</b><br>Nadir locked",
            showarrow=True,
            arrowhead=2,
            arrowsize=1,
            arrowwidth=2,
            arrowcolor="blue",
            ax=-100,
            ay=-60,
            bgcolor="rgba(100, 200, 255, 0.85)",
            bordercolor="blue",
            borderwidth=2,
            font=dict(size=11),
            align="left"
        )
    
    fig.update_layout(
        title="Nadir Pointing: Error Euler Angle About Each Axis",
        xaxis_title="Time (hours)",
        yaxis_title="Error (degrees)",
        hovermode='x unified',
        template="plotly_white",
        height=600,
        width=1000,
        showlegend=True,
        legend=dict(x=0.02, y=0.98)
    )
    
    fig.update_yaxes(zeroline=True)
    
    return fig


# ============================================================================
# EXAMPLE 3: Sun angle with callout showing satellite orientation
# ============================================================================

def create_sun_angle_plot(sun_df):
    """
    Create sun angle plot with annotations
    """
    fig = go.Figure()
    
    time_hours = sun_df["time.1"]/3600
    
    fig.add_trace(go.Scatter(
        x=time_hours,
        y=sun_df["SunAngle"],
        name="Sun angle",
        mode='lines',
        line=dict(color='orange', width=3),
        fill='tozeroy',
        fillcolor='rgba(255, 165, 0, 0.2)'
    ))
    
    # Add reference line
    fig.add_hline(y=8, line_dash="dash", line_color="red", 
                  annotation_text="8° threshold", annotation_position="right")
    
    # Add callouts
    fig.add_annotation(
        x=5, y=45,
        text="<b>Sun Avoidance Mode</b><br>Sun angle > 8°",
        showarrow=True,
        arrowhead=2,
        arrowsize=1,
        arrowwidth=2,
        arrowcolor="red",
        ax=100,
        ay=-80,
        bgcolor="rgba(255, 150, 150, 0.85)",
        bordercolor="red",
        borderwidth=2,
        font=dict(size=11)
    )
    
    fig.add_annotation(
        x=15, y=3,
        text="<b>Sun-Safe</b><br>Sun angle < 8°",
        showarrow=True,
        arrowhead=2,
        arrowsize=1,
        arrowwidth=2,
        arrowcolor="green",
        ax=-80,
        ay=60,
        bgcolor="rgba(150, 255, 150, 0.85)",
        bordercolor="green",
        borderwidth=2,
        font=dict(size=11)
    )
    
    fig.update_layout(
        title="Sun Angle During Mission",
        xaxis_title="Time (hours)",
        yaxis_title="Sun Angle (degrees)",
        hovermode='x unified',
        template="plotly_white",
        height=600,
        width=1000,
        showlegend=False
    )
    
    fig.update_yaxes(range=[0, max(sun_df["SunAngle"])*1.1])
    
    return fig


# ============================================================================
# EXAMPLE 4: Advanced - Multi-subplot with coordinated callouts
# ============================================================================

def create_combined_attitude_plot(detumbling_df, nadir_df, sun_df):
    """
    Create a 3-panel plot showing attitude control progression
    """
    fig = make_subplots(
        rows=3, cols=1,
        subplot_titles=(
            "Detumbling: Angular Velocity",
            "Nadir Pointing: Error Euler Angles",
            "Sun Angle"
        ),
        vertical_spacing=0.12,
        specs=[[{"secondary_y": False}],
               [{"secondary_y": False}],
               [{"secondary_y": False}]]
    )
    
    # Row 1: Detumbling
    fig.add_trace(
        go.Scatter(x=detumbling_df["time.1"]/60, 
                   y=detumbling_df["Spacecraft Dynamics:4(1)"],
                   name="x (detumble)", line=dict(color='blue'), mode='lines'),
        row=1, col=1
    )
    fig.add_trace(
        go.Scatter(x=detumbling_df["time.1"]/60, 
                   y=detumbling_df["Spacecraft Dynamics:4(2)"],
                   name="y (detumble)", line=dict(color='red'), mode='lines'),
        row=1, col=1
    )
    fig.add_trace(
        go.Scatter(x=detumbling_df["time.1"]/60, 
                   y=detumbling_df["Spacecraft Dynamics:4(3)"],
                   name="z (detumble)", line=dict(color='green'), mode='lines'),
        row=1, col=1
    )
    fig.add_hline(y=1, line_dash="dash", line_color="gray", row=1, col=1)
    
    # Row 2: Nadir
    time_nadir = nadir_df["time"]/3600
    fig.add_trace(
        go.Scatter(x=time_nadir, 
                   y=np.rad2deg(nadir_df["Attitude Control:1(1,1)"]),
                   name="x error", line=dict(color='blue'), mode='lines'),
        row=2, col=1
    )
    fig.add_trace(
        go.Scatter(x=time_nadir, 
                   y=np.rad2deg(nadir_df["Attitude Control:1(2,1)"]),
                   name="y error", line=dict(color='red'), mode='lines'),
        row=2, col=1
    )
    fig.add_trace(
        go.Scatter(x=time_nadir, 
                   y=np.rad2deg(nadir_df["Attitude Control:1(3,1)"]),
                   name="z error", line=dict(color='green'), mode='lines'),
        row=2, col=1
    )
    fig.add_hline(y=8, line_dash="dash", line_color="gray", row=2, col=1)
    
    # Row 3: Sun angle
    time_sun = sun_df["time.1"]/3600
    fig.add_trace(
        go.Scatter(x=time_sun, 
                   y=sun_df["SunAngle"],
                   name="Sun angle", line=dict(color='orange', width=2), 
                   fill='tozeroy', fillcolor='rgba(255, 165, 0, 0.2)', mode='lines'),
        row=3, col=1
    )
    fig.add_hline(y=8, line_dash="dash", line_color="red", row=3, col=1)
    
    # Update axes labels
    fig.update_xaxes(title_text="Time (min)", row=1, col=1)
    fig.update_xaxes(title_text="Time (hours)", row=2, col=1)
    fig.update_xaxes(title_text="Time (hours)", row=3, col=1)
    
    fig.update_yaxes(title_text="Angular Velocity (deg/s)", row=1, col=1)
    fig.update_yaxes(title_text="Error (degrees)", row=2, col=1)
    fig.update_yaxes(title_text="Sun Angle (degrees)", row=3, col=1)
    
    fig.update_layout(
        height=1000,
        width=1000,
        showlegend=True,
        template="plotly_white",
        hovermode='x unified',
        title_text="CubeSat Attitude Control Mission Timeline"
    )
    
    return fig


# ============================================================================
# USAGE EXAMPLE
# ============================================================================

if __name__ == "__main__":
    # Generate sample data (replace with your actual dataframes)
    # These are just dummy data for demonstration
    
    try:
        detumbling_df
        nadir_df
        sun_df
    except NameError:
        detumbling_df = pd.read_excel("WorkingDetumbling.xlsx", usecols=["time.1", "Spacecraft Dynamics:4(1)", "Spacecraft Dynamics:4(2)", "Spacecraft Dynamics:4(3)"])
        nadir_df = pd.read_excel("WorkingPIDNadir.xlsx", usecols=["time", "Attitude Control:1(1,1)", "Attitude Control:1(2,1)", "Attitude Control:1(3,1)"])
        sun_df = pd.read_excel("WorkingPiDSun.xlsx", usecols=["time.1", "SunAngle"])
    
    # Create individual plots
    fig1 = create_detumbling_plot(detumbling_df)
    fig1.show()
    
    fig2 = create_nadir_plot_with_boxes(nadir_df)
    fig2.show()
    
    fig3 = create_sun_angle_plot(sun_df)
    fig3.show()
    
    # Create combined plot
    fig4 = create_combined_attitude_plot(detumbling_df, nadir_df, sun_df)
    fig4.show()